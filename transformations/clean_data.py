from typing import List


def upper_case_names(names: List) -> List:
    return list(map(str.upper, names))


def remove_whitespaces_from_names(names: List) -> List:
    return [name.strip().replace(' ', '_') for name in names]
