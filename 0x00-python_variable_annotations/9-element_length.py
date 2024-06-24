#!/usr/bin/env python3
"""
Annotating a given function
"""
from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    returns a list of tuples that contains
    Sequence(i) and length if it
    """
    return [(i, len(i)) for i in lst]
