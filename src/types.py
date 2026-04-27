from enum import Enum


class PLCType(Enum):
    INT = "int"
    FLOAT = "float"
    BOOL = "bool"
    STRING = "string"
    # ====================================================================
    # EXTENSION: FILE — handle for the fopen/fappend extension.
    # No code letter (it never appears as a `T` tag in instructions).
    # ====================================================================
    FILE = "FILE"
    ERROR = "error"

    @property
    def code(self) -> str:
        # Single-letter type tag used in the stack-machine instructions
        # (e.g. "add I", "push F 1.5"). ERROR / FILE have no code.
        return {
            PLCType.INT: "I",
            PLCType.FLOAT: "F",
            PLCType.BOOL: "B",
            PLCType.STRING: "S",
        }[self]


def default_value(t: PLCType):
    return {
        PLCType.INT: 0,
        PLCType.FLOAT: 0.0,
        PLCType.BOOL: False,
        PLCType.STRING: "",
        PLCType.FILE: None,  # opened only by `fopen`
    }[t]


def can_implicitly_convert(src: PLCType, dst: PLCType) -> bool:
    # The spec only allows int -> float.
    if src == dst:
        return True
    return src == PLCType.INT and dst == PLCType.FLOAT
