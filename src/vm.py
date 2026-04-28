"""Stack-based virtual machine for the PLC project."""

from __future__ import annotations
import shlex
import sys
from typing import Callable

_ESCAPES = {"n": "\n", "t": "\t", "r": "\r", '"': '"', "\\": "\\"}

def _unescape(s: str) -> str:
    out: list[str] = []
    i = 0
    while i < len(s):
        c = s[i]
        if c == "\\" and i + 1 < len(s) and s[i + 1] in _ESCAPES:
            out.append(_ESCAPES[s[i + 1]]); i += 2
        else:
            out.append(c); i += 1
    return "".join(out)

def _parse_value(t: str, raw: str):
    if t == "I": return int(raw)
    if t == "F": return float(raw)
    if t == "B": return raw == "true"
    if t == "S":
        if len(raw) >= 2 and raw[0] == '"' and raw[-1] == '"':
            return _unescape(raw[1:-1])
        return raw
    raise ValueError(f"unknown type tag '{t}'")


class StackVM:
    def __init__(self, program: str, stdin=None, stdout=None):
        self._instr: list[list[str]] = []
        for raw_line in program.splitlines():
            line = raw_line.strip()
            if not line: continue
            self._instr.append(shlex.split(line, posix=False))
        self._labels: dict[int, int] = {}
        for ip, parts in enumerate(self._instr):
            if parts[0] == "label":
                self._labels[int(parts[1])] = ip

        self.stack: list = []
        self.vars: dict[str, object] = {}
        self.stdin  = stdin  if stdin  is not None else sys.stdin
        self.stdout = stdout if stdout is not None else sys.stdout

        self._dispatch: dict[str, Callable[[list[str]], None]] = {
            "add": self.op_add, "sub": self.op_sub,
            "mul": self.op_mul, "div": self.op_div,
            "mod": self.op_mod, "uminus": self.op_uminus,
            "concat": self.op_concat,
            "and": self.op_and, "or": self.op_or, "not": self.op_not,
            "gt": self.op_gt, "lt": self.op_lt, "eq": self.op_eq,
            "itof": self.op_itof,
            "push": self.op_push, "pop": self.op_pop,
            "load": self.op_load, "save": self.op_save,
            "label": self.op_nop,
            "jmp": self.op_jmp, "fjmp": self.op_fjmp,
            "print": self.op_print, "read": self.op_read,
            # EXTENSION: array
            "createarray": self.op_createarray,
            "loadarray":   self.op_loadarray,
            "savearray":   self.op_savearray,
        }

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

    # --- zakladne instrukcie ---------------------------------------------

    def op_nop(self, parts):    return None
    def op_pop(self, parts):    self.stack.pop()
    def op_load(self, parts):   self.stack.append(self.vars[parts[1]])
    def op_save(self, parts):   self.vars[parts[1]] = self.stack.pop()
    def op_itof(self, parts):   self.stack.append(float(self.stack.pop()))
    def op_not(self, parts):    self.stack.append(not bool(self.stack.pop()))
    def op_uminus(self, parts): self.stack.append(-self.stack.pop())
    def op_jmp(self, parts):    return self._labels[int(parts[1])]

    def op_push(self, parts):
        t = parts[1]
        raw = " ".join(parts[2:])
        self.stack.append(_parse_value(t, raw))

    def op_add(self, parts):
        b = self.stack.pop(); a = self.stack.pop(); self.stack.append(a + b)
    def op_sub(self, parts):
        b = self.stack.pop(); a = self.stack.pop(); self.stack.append(a - b)
    def op_mul(self, parts):
        b = self.stack.pop(); a = self.stack.pop(); self.stack.append(a * b)
    def op_div(self, parts):
        b = self.stack.pop(); a = self.stack.pop()
        self.stack.append(int(a / b) if parts[1] == "I" else a / b)
    def op_mod(self, parts):
        b = self.stack.pop(); a = self.stack.pop(); self.stack.append(a % b)
    def op_concat(self, parts):
        b = self.stack.pop(); a = self.stack.pop(); self.stack.append(a + b)
    def op_and(self, parts):
        b = self.stack.pop(); a = self.stack.pop()
        self.stack.append(bool(a) and bool(b))
    def op_or(self, parts):
        b = self.stack.pop(); a = self.stack.pop()
        self.stack.append(bool(a) or bool(b))
    def op_gt(self, parts):
        b = self.stack.pop(); a = self.stack.pop(); self.stack.append(a > b)
    def op_lt(self, parts):
        b = self.stack.pop(); a = self.stack.pop(); self.stack.append(a < b)
    def op_eq(self, parts):
        b = self.stack.pop(); a = self.stack.pop(); self.stack.append(a == b)

    def op_fjmp(self, parts):
        v = self.stack.pop()
        if not v: return self._labels[int(parts[1])]
        return None

    def op_print(self, parts):
        n = int(parts[1])
        if n == 0: return
        values = self.stack[-n:]
        del self.stack[-n:]
        for v in values:
            self.stdout.write(self._format(v) + "\n")

    def op_read(self, parts):
        t = parts[1]
        line = self.stdin.readline()
        if not line: raise RuntimeError("read: unexpected end of input")
        line = line.rstrip("\n").rstrip("\r")
        if t == "I":   self.stack.append(int(line))
        elif t == "F": self.stack.append(float(line))
        elif t == "B": self.stack.append(line.strip() == "true")
        else:          self.stack.append(line)

    @staticmethod
    def _format(v) -> str:
        if isinstance(v, bool): return "true" if v else "false"
        return str(v)

    # ====================================================================
    # EXTENSION: array instrukcie
    # ====================================================================

    def op_createarray(self, parts):
        # createarray a 10 — vytvor pole menom 'a' s N nulami, uloz do vars
        name = parts[1]       # meno pola napr. "a"
        n = int(parts[2])     # velkost pola napr. 10
        self.vars[name] = [0] * n   # vytvor Python zoznam nul

    def op_loadarray(self, parts):
        # loadarray a — vezmi index a pole zo zasobnika, daj hodnotu na zasobnik
        name = parts[1]           # meno pola (pre chybovu hlasku)
        idx = self.stack.pop()    # index napr. 1
        arr = self.stack.pop()    # pole — Python zoznam
        if not 0 <= idx < len(arr):
            raise RuntimeError(f"loadarray: index {idx} out of bounds for '{name}'")
        self.stack.append(arr[idx])   # daj hodnotu na zasobnik

    def op_savearray(self, parts):
        # savearray a — vezmi index, pole a hodnotu zo zasobnika, uloz do pola
        name = parts[1]           # meno pola
        idx   = self.stack.pop()  # index napr. 1
        arr   = self.stack.pop()  # pole — Python zoznam
        value = self.stack.pop()  # hodnota napr. 5
        if not 0 <= idx < len(arr):
            raise RuntimeError(f"savearray: index {idx} out of bounds for '{name}'")
        arr[idx] = value          # uloz hodnotu
        self.vars[name] = arr     # uloz pole spat do premennych


# ===========================================================================
# VYSVETLENIE PRE OBHAJOBU
# ===========================================================================
# Co robi VM?
#   Vykonava instrukcie ktore vygeneroval CodeGenerator.
#   Ma zasobnik (stack) kde prebieha vypocet.
#   Zasobnik = hromada hodnot — push prida, pop odoberie z vrchu.
#
# op_createarray — pre instrukciu "createarray a 10"
#   Vytvori Python zoznam 10 nul a ulozi ho priamo do vars["a"]
#   (nedava na zasobnik — pole je prilis velke)
#
# op_loadarray — pre instrukciu "loadarray a"
#   Vezme zo zasobnika: index (napr. 1) a pole
#   Daj na zasobnik hodnotu pole[index]
#
# op_savearray — pre instrukciu "savearray a"
#   Vezme zo zasobnika: index, pole a hodnotu
#   Ulozi hodnotu do pole[index] a pole spat do vars
#
# Prklad pre "a[1] = 5; write a[1];"
#   createarray a 10  → vars["a"] = [0,0,0,0,0,0,0,0,0,0]
#   push I 5          → stack: [5]
#   load a            → stack: [5, [0,0,...]]
#   push I 1          → stack: [5, [0,0,...], 1]
#   savearray a       → arr[1]=5, stack: []
#   load a            → stack: [[0,5,0,...]]
#   push I 1          → stack: [[0,5,...], 1]
#   loadarray a       → stack: [5]
#   print 1           → vypise: 5
# ===========================================================================