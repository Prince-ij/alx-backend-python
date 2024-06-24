#!/usr/bin/env python3
"""
Duck typing: The input types aren't known
"""
from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ just getting the first element
    all about duck typing though
    """
    if lst:
        return lst[0]
    else:
        return None
