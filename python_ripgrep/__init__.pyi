import enum

class PySortMode:
    kind: PySortModeKind
    reverse: bool = False

    def __init__(self, kind: PySortModeKind, reverse: bool = False): ...

class PySortModeKind(enum.Enum):
    Path = enum.auto()
    LastModified = enum.auto()
    LastAccessed = enum.auto()
    Created = enum.auto()

def search(
    patterns: list[str],
    paths: list[str] | None = None,
    globs: list[str] | None = None,
    heading: bool | None = None,
    after_context: int | None = None,
    before_context: int | None = None,
    separator_field_context: str | None = None,
    separator_field_match: str | None = None,
    separator_context: str | None = None,
    sort: PySortMode | None = None,
    max_count: int | None = None,
    line_number: bool | None = None,
    multiline: bool | None = None,
    hidden: bool | None = None,
) -> list[str]: ...
def files(
    patterns: list[str],
    paths: list[str] | None = None,
    globs: list[str] | None = None,
    heading: bool | None = None,
    after_context: int | None = None,
    before_context: int | None = None,
    separator_field_context: str | None = None,
    separator_field_match: str | None = None,
    separator_context: str | None = None,
    sort: PySortMode | None = None,
    max_count: int | None = None,
    line_number: bool | None = None,
    multiline: bool | None = None,
    hidden: bool | None = None,
) -> list[str]: ...
