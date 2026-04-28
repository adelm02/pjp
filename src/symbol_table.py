from .types import PLCType


class SymbolTable:
    def __init__(self):
        self._symbols: dict[str, PLCType] = {}

    def declare(self, name: str, t: PLCType) -> bool:
        if name in self._symbols:
            return False
        self._symbols[name] = t
        return True

    def is_declared(self, name: str) -> bool:
        return name in self._symbols

    def type_of(self, name: str) -> PLCType:
        return self._symbols.get(name, PLCType.ERROR)

    def all_symbols(self) -> dict[str, PLCType]:
        return dict(self._symbols)
