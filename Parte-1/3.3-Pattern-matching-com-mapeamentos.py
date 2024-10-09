from collections import OrderedDict


def get_creators(record: dict) -> list:
    match record:
        case {"type": "book", "api": 2, "authors": [*names]}:  # (1)
            return names
        case {"type": "book", "api": 1, "author": name}:  # (2)
            return [name]
        case {"type": "book"}:  # (3)
            raise ValueError(f"Invalid 'book' record: {record!r}")
        case {"type": "movie", "director": name}:  # (4)
            return [name]
        case _:  # (5)
            raise ValueError(f"Invalid record: {record!r}")


b1 = dict(api=1, author="Douglas Hofstadter", type="book", title="Gödel, Escher, Bach")

b2 = OrderedDict(
    api=2,
    type="book",
    title="Python in a Nutshell",
    authors="Martelli Ravenscroft Holden".split(),
)
