"""Stack-based virtual machine for the PLC project.

Reads a textual program in the instruction format defined by the assignment
(one instruction per line, whitespace-separated tokens) and executes it.
"""

from __future__ import annotations

import shlex
import sys
from typing import Callable


_ESCAPES = {"n": "\n", "t": "\t", "r": "\r", '"': '"', "\\": "\\"}


def _unescape(s: str) -> str:
    """Decode the small set of C-style escape sequences we support
    (\\n, \\t, \\r, \\", \\\\). Other backslash pairs are left alone."""
    out: list[str] = []
    i = 0
    while i < len(s):
        c = s[i]
        if c == "\\" and i + 1 < len(s) and s[i + 1] in _ESCAPES:
            out.append(_ESCAPES[s[i + 1]])
            i += 2
        else:
            out.append(c)
            i += 1
    return "".join(out)


def _parse_value(t: str, raw: str):
    if t == "I":
        return int(raw)
    if t == "F":
        return float(raw)
    if t == "B":
        return raw == "true"
    if t == "S":
        if len(raw) >= 2 and raw[0] == '"' and raw[-1] == '"':
            return _unescape(raw[1:-1])
        return raw
    raise ValueError(f"unknown type tag '{t}'")


class StackVM:
    def __init__(self, program: str, stdin=None, stdout=None):
        # Tokenize each line. Use posix=False so quotes around strings are
        # preserved verbatim — we strip them ourselves in op_push so we keep
        # full control over the escape-sequence handling.
        self._instr: list[list[str]] = []
        for raw_line in program.splitlines():
            line = raw_line.strip()
            if not line:
                continue
            self._instr.append(shlex.split(line, posix=False))
        self._labels: dict[int, int] = {}
        for ip, parts in enumerate(self._instr):
            if parts[0] == "label":
                self._labels[int(parts[1])] = ip

        self.stack: list = []
        self.vars: dict[str, object] = {}
        self.stdin = stdin if stdin is not None else sys.stdin
        self.stdout = stdout if stdout is not None else sys.stdout

        # Open file handles per FILE variable (extension-only).
        self._files: dict[int, object] = {}

        # Dispatch table — extensions (charAt, fopen, fappend, ...) plug in
        # by adding a single entry here plus a method.
        self._dispatch: dict[str, Callable[[list[str]], None]] = {
            "add": self.op_add,
            "sub": self.op_sub,
            "mul": self.op_mul,
            "div": self.op_div,
            "mod": self.op_mod,
            "uminus": self.op_uminus,
            "concat": self.op_concat,
            "and": self.op_and,
            "or": self.op_or,
            "not": self.op_not,
            "gt": self.op_gt,
            "lt": self.op_lt,
            "eq": self.op_eq,
            "itof": self.op_itof,
            "push": self.op_push,
            "pop": self.op_pop,
            "load": self.op_load,
            "save": self.op_save,
            "label": self.op_nop,
            "jmp": self.op_jmp,
            "fjmp": self.op_fjmp,
            "print": self.op_print,
            "read": self.op_read,
            # ============================================================
            # EXTENSION: charAt
            # ============================================================
            "charAt": self.op_charAt,
            # ============================================================
            # EXTENSION: FILE / fopen / fappend
            # ============================================================
            "fopen": self.op_fopen,
            "fappend": self.op_fappend,
            "open": self.op_open,
            "fwrite": self.op_fwrite,
        }

    # --- main loop -------------------------------------------------------

    def run(self):
        ip = 0
        n = len(self._instr)
        while ip < n:
            parts = self._instr[ip]
            op = parts[0]
            handler = self._dispatch.get(op)
            if handler is None:
                raise RuntimeError(f"unknown instruction '{op}'")
            new_ip = handler(parts)
            ip = new_ip if new_ip is not None else ip + 1

    # --- ops -------------------------------------------------------------

    def op_nop(self, parts):
        return None

    def op_push(self, parts):
        # `push T x` — `x` is the rest of the line. For strings, posix=False
        # leaves the surrounding quotes intact; _parse_value strips them and
        # decodes escape sequences.
        t = parts[1]
        raw = " ".join(parts[2:])
        self.stack.append(_parse_value(t, raw))

    def op_pop(self, parts):
        self.stack.pop()

    def op_load(self, parts):
        self.stack.append(self.vars[parts[1]])

    def op_save(self, parts):
        self.vars[parts[1]] = self.stack.pop()

    def op_add(self, parts):
        b = self.stack.pop(); a = self.stack.pop()
        self.stack.append(a + b)

    def op_sub(self, parts):
        b = self.stack.pop(); a = self.stack.pop()
        self.stack.append(a - b)

    def op_mul(self, parts):
        b = self.stack.pop(); a = self.stack.pop()
        self.stack.append(a * b)

    def op_div(self, parts):
        b = self.stack.pop(); a = self.stack.pop()
        if parts[1] == "I":
            # Integer division per the spec — truncate towards zero.
            self.stack.append(int(a / b))
        else:
            self.stack.append(a / b)

    def op_mod(self, parts):
        b = self.stack.pop(); a = self.stack.pop()
        self.stack.append(a % b)

    def op_uminus(self, parts):
        self.stack.append(-self.stack.pop())

    def op_concat(self, parts):
        b = self.stack.pop(); a = self.stack.pop()
        self.stack.append(a + b)

    def op_and(self, parts):
        b = self.stack.pop(); a = self.stack.pop()
        self.stack.append(bool(a) and bool(b))

    def op_or(self, parts):
        b = self.stack.pop(); a = self.stack.pop()
        self.stack.append(bool(a) or bool(b))

    def op_not(self, parts):
        self.stack.append(not bool(self.stack.pop()))

    def op_gt(self, parts):
        b = self.stack.pop(); a = self.stack.pop()
        self.stack.append(a > b)

    def op_lt(self, parts):
        b = self.stack.pop(); a = self.stack.pop()
        self.stack.append(a < b)

    def op_eq(self, parts):
        b = self.stack.pop(); a = self.stack.pop()
        self.stack.append(a == b)

    def op_itof(self, parts):
        self.stack.append(float(self.stack.pop()))

    def op_jmp(self, parts):
        return self._labels[int(parts[1])]

    def op_fjmp(self, parts):
        v = self.stack.pop()
        if not v:
            return self._labels[int(parts[1])]
        return None

    def op_print(self, parts):
        n = int(parts[1])
        if n == 0:
            return
        values = self.stack[-n:]
        del self.stack[-n:]
        for v in values:
            self.stdout.write(self._format(v) + "\n")

    def op_read(self, parts):
        t = parts[1]
        line = self.stdin.readline()
        if not line:
            raise RuntimeError("read: unexpected end of input")
        line = line.rstrip("\n").rstrip("\r")
        if t == "I":
            self.stack.append(int(line))
        elif t == "F":
            self.stack.append(float(line))
        elif t == "B":
            self.stack.append(line.strip() == "true")
        else:  # S
            self.stack.append(line)

    @staticmethod
    def _format(v) -> str:
        if isinstance(v, bool):
            return "true" if v else "false"
        return str(v)

    # ====================================================================
    # EXTENSION: charAt — string × int -> 1-char string
    # ====================================================================
    def op_charAt(self, parts):
        idx = self.stack.pop()
        s = self.stack.pop()
        if not 0 <= idx < len(s):
            raise RuntimeError(f"charAt: index {idx} out of bounds for string of length {len(s)}")
        self.stack.append(s[idx])

    # ====================================================================
    # EXTENSION: FILE / fopen / fappend
    #   The file handle stored in a variable is a small int id; the actual
    #   Python file object lives in self._files[id].
    # ====================================================================
    def op_fopen(self, parts):
        path = self.stack.pop()
        handle_id = len(self._files) + 1
        # "append" mode so multiple `fopen` calls don't truncate; matches the
        # spirit of `fappend`.
        self._files[handle_id] = open(path, "a", encoding="utf-8")
        self.stack.append(handle_id)

    def op_fappend(self, parts):
        # Two calling conventions:
        #   `fappend N`  — V1: pops N values total (file handle deepest,
        #                  N-1 values to write).
        #   `fappend`    — V2: pops 1 value to write; file handle stays on
        #                  the stack so the next `fappend` can reuse it.
        if len(parts) == 1:
            value = self.stack.pop()
            handle_id = self.stack[-1]            # peek: keep on stack
            f = self._files[handle_id]
            f.write(self._format(value))
            f.flush()
            return
        n = int(parts[1])
        if n < 1:
            return
        values = self.stack[-n + 1:] if n > 1 else []
        del self.stack[-n + 1:]
        handle_id = self.stack.pop()
        f = self._files[handle_id]
        for v in values:
            f.write(self._format(v))
        f.flush()
        
    def op_open(self, parts):
        # stejná logika jako fopen — otevři soubor, dej handle na zásobník
        path = self.stack.pop()
        handle_id = len(self._files) + 1
        self._files[handle_id] = open(path, "a", encoding="utf-8")
        self.stack.append(handle_id)

    def op_fwrite(self, parts):
        # fwrite N — vezme N hodnot + file handle ze zásobníku a zapíše je
        n = int(parts[1])          # počet výrazů
        values = self.stack[-n:]   # vezmi N hodnot ze zásobníku
        del self.stack[-n:]        # smaž je ze zásobníku
        handle_id = self.stack.pop()  # vezmi file handle
        f = self._files[handle_id]
        for v in values:
            f.write(self._format(v))
        f.flush()