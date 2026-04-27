# PLC Project (PJP)
## Setup

```bash
pip install -r requirements.txt
# Regenerate the ANTLR parser (only needed if grammar/PLC.g4 changes):
bash tools/gen_antlr.sh
```

Java is required only to run the ANTLR generator. The compiled parser is pure Python.

## Running

```bash
# Compile a program; print the generated stack-machine code to stdout:
python -m src.main examples/sample1.plc

# Compile and write the generated code to a file:
python -m src.main examples/sample1.plc --out out.code

# Compile and execute on the bundled stack VM:
python -m src.main examples/sample1.plc --run

# Demonstrate full error reporting (all syntax + type errors at once):
python -m src.main examples/errors.plc
```

## Layout

- `grammar/PLC.g4` — ANTLR4 grammar (base + all extensions).
- `generated/` — ANTLR‑generated lexer/parser/visitor (regenerated from grammar).
- `src/error_listener.py` — collects every syntax error rather than aborting on the first.
- `src/types.py`, `src/symbol_table.py` — supporting types.
- `src/type_checker.py` — visitor that annotates expression nodes and reports type errors.
- `src/code_generator.py` — visitor that emits the textual stack‑machine program.
- `src/vm.py` — stack interpreter (with handlers for the extension opcodes).
- `src/main.py` — CLI entry point.
- `examples/` — sample programs (base + extensions + intentionally broken).

## Verification against the official reference

`examples/official_t{1,2,3}.plc` and `examples/official_errors.plc` are downloaded
from `linedu.vsb.cz/~beh01/wiki_data/`. Generated output of all three programs
matches the official `.expected` whitespace‑normalized:

```bash
for n in 1 2 3; do
  diff -bw <(python -m src.main examples/official_t$n.plc 2>/dev/null) \
            examples/official_t$n.expected && echo "t$n IDENTICAL"
done
```

## Extensions

The grammar and the visitors include **all four** known cviko extensions
from `../PJP_Upravy/`. Each extension is bracketed in the source by
`// EXTENSION: NAME` comment blocks so it's easy to see / disable / pick
the right one for the practical session.

| # | Extension | Demo program | Notes |
|---|---|---|---|
| 1 | `charAt` (`s[i]`) | `examples/ext_charat.plc` | Postfix index on a string. Returns a 1‑character string. New VM opcode `charAt`. |
| 2 | `FILE`, `fopen`, `fappend` — **VARIANT 1 (Běhálek)** | `examples/ext_file_v1.plc` | Syntax `fopen f, "path"; fappend f, v1, v2, …;`. Codegen emits `fappend N` (file handle counted in N). |
| 2 | `FILE`, `fopen`, `fappend` — **VARIANT 2 (Vašínek)** | `examples/ext_file_v2.plc` | Syntax `f << v1 << v2 << …;`. Codegen emits chained `fappend` (no count) and a final `pop`. Both variants share the same `FILE` declaration. |
| 3 | Ternary `cond ? a : b` | `examples/ext_ternary.plc` | Right‑associative; precedence between `\|\|` and `=`. Type rule: `cond` must be `bool`, branches share a common (numeric or equal) type. |
| 4 | `for (init; cond; step) stmt` (Vašínek) | `examples/ext_for.plc` | Lowered to the equivalent `while`. `cond` must be `bool`; `init` and `step` are arbitrary expressions whose values are discarded. |

### Which one to pick on the cviko

Watch for the announcement during the practical session and remove (or simply
ignore) the other three. The extensions are independent — leaving them all
enabled does not break the base. To remove an extension, delete:

- The `// EXTENSION: NAME` block in `grammar/PLC.g4`,
- The matching visitor methods in `src/type_checker.py` and
  `src/code_generator.py` (also bracketed by `// EXTENSION: NAME`),
- The dispatch‑table entries and methods in `src/vm.py` (same brackets),
- The corresponding example `examples/ext_*.plc`.

After removing grammar pieces, regenerate the parser via
`bash tools/gen_antlr.sh`.

## New stack‑machine instructions added by the extensions

| Instruction | Used by | Description |
|---|---|---|
| `charAt` | charAt extension | Pops int idx and string s, pushes 1‑char string `s[idx]`. |
| `fopen` | FILE extension | Pops string path, opens it (append mode), pushes a file handle. |
| `fappend N` | FILE V1 | Pops N values total: file handle (deepest) + N−1 values to write. File is consumed. |
| `fappend` | FILE V2 | Pops one value, writes it to the file handle currently on top of stack (which stays). Closing `pop` drops the handle. |
