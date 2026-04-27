"""Entry point for the PLC compiler/interpreter.

Pipeline:
    parse  ->  type-check  ->  generate stack-machine code  ->  (optional) run
The first failing stage prints all of its errors and exits non-zero.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

# Make `generated/` and `src/` importable when invoked as `python -m src.main`
# or as a plain script. The repository layout intentionally keeps `generated`
# as a sibling of `src`, so we add the project root to sys.path.
_ROOT = Path(__file__).resolve().parent.parent
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from antlr4 import CommonTokenStream, InputStream  # noqa: E402

from generated.PLCLexer import PLCLexer  # noqa: E402
from generated.PLCParser import PLCParser  # noqa: E402

from src.code_generator import PLCCodeGenerator  # noqa: E402
from src.error_listener import CollectingErrorListener  # noqa: E402
from src.type_checker import PLCTypeChecker  # noqa: E402
from src.vm import StackVM  # noqa: E402


def compile_file(input_path: str) -> tuple[str | None, list[str]]:
    """Returns (generated_code, errors). On any error, generated_code is None
    and errors lists every problem found in the earliest failing stage."""

    # `utf-8-sig` strips a byte-order mark if the source file has one. The
    # official `.plc` test files on the wiki are saved with a BOM, and
    # ANTLR's FileStream would otherwise treat it as an unknown character.
    text = Path(input_path).read_text(encoding="utf-8-sig")
    stream = InputStream(text)
    lexer = PLCLexer(stream)
    lexer_listener = CollectingErrorListener()
    lexer.removeErrorListeners()
    lexer.addErrorListener(lexer_listener)

    tokens = CommonTokenStream(lexer)
    parser = PLCParser(tokens)
    parser_listener = CollectingErrorListener()
    parser.removeErrorListeners()
    parser.addErrorListener(parser_listener)

    tree = parser.program()

    syntax_errors = lexer_listener.errors + parser_listener.errors
    if syntax_errors:
        return None, syntax_errors

    checker = PLCTypeChecker()
    checker.visit(tree)
    if checker.errors:
        return None, checker.errors

    codegen = PLCCodeGenerator(checker.symbols, checker.needs_itof)
    return codegen.generate(tree), []


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="PLC compiler / interpreter")
    ap.add_argument("input", help="Path to a .plc source file")
    ap.add_argument("--out", "-o", help="Write generated code to this file")
    ap.add_argument("--run", action="store_true", help="Execute generated code on the VM")
    args = ap.parse_args(argv)

    code, errors = compile_file(args.input)
    if errors:
        for e in errors:
            print(e, file=sys.stderr)
        return 1

    if args.out:
        Path(args.out).write_text(code, encoding="utf-8")
    else:
        sys.stdout.write(code)

    if args.run:
        StackVM(code).run()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
