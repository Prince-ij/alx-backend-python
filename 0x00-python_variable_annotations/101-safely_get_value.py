#!/usr/bin/env python3
"""
Annotating a function part2 : Duck typing
"""
from typing import Mapping, Any


def safely_get_value(dct: Mapping[Any, Any], key: Any, default: Any = None) -> Any:
    """ documentation already in module """
    if key in dct:
        return dct[key]
    else:
        return default
