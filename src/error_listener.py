from antlr4.error.ErrorListener import ErrorListener


class CollectingErrorListener(ErrorListener):
    """Collects every syntax error so we can report them all (the spec
    requires that the compiler reports *all* syntax errors, not just the
    first one)."""

    def __init__(self):
        super().__init__()
        self.errors: list[str] = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.errors.append(f"[syntax] line {line}:{column} {msg}")

    @property
    def has_errors(self) -> bool:
        return len(self.errors) > 0
