"""Generic pagination helper used by list-heavy commands and API routes."""
from dataclasses import dataclass
from typing import Generic, Sequence, TypeVar

T = TypeVar("T")


@dataclass
class Page(Generic[T]):
    items: Sequence[T]
    page: int
    page_size: int
    total: int

    @property
    def total_pages(self) -> int:
        return max(1, -(-self.total // self.page_size))


def paginate(items: Sequence[T], page: int = 1, page_size: int = 20) -> Page[T]:
    start = (page - 1) * page_size
    return Page(items=items[start : start + page_size], page=page, page_size=page_size, total=len(items))
