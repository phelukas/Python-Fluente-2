from dataclasses import dataclass, field
from typing import Optional
from enum import Enum, auto
from datetime import date as dt


"""
@dataclass(*, init=True, repr=True, eq=True, order=False,
              unsafe_hash=False, frozen=False)
"""


@dataclass
class ClubMember:
    name: str
    guests: list[str] = field(default_factory=list)
    thlete: bool = field(default=False, repr=False)


@dataclass
class HackerClubMember(ClubMember):
    all_handles = set()
    handle: str = ""

    def __post_init__(self):
        cls = self.__class__
        if self.handle == "":
            self.handle = self.name.split()[0]
        if self.handle in cls.all_handles:
            msg = f"handle {self.handle!r} already exists."
            raise ValueError(msg)
        cls.all_handles.add(self.handle)


class ResourceType(Enum):
    BOOK = auto()
    EBOOK = auto()
    VIDEO = auto()


@dataclass
class Resource:
    """Media resource description."""

    identifier: str
    title: str = "<untitled>"
    creators: list[str] = field(default_factory=list)
    date: Optional[dt] = None
    type: ResourceType = ResourceType.BOOK
    description: str = ""
    language: str = ""
    subjects: list[str] = field(default_factory=list)


description = "Improving the design of existing code"
book = Resource(
    "978-0-13-475759-9",
    "Refactoring, 2nd Edition",
    ["Martin Fowler", "Kent Beck"],
    dt(2018, 11, 19),
    ResourceType.BOOK,
    description,
    "EN",
    ["computer programming", "OOP"],
)
book
