#!/usr/bin/env python3
"""
Annotating a function part2 : Duck typing
"""
from typing import Mapping, Any, Union, TypeVar
T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) -> Union[T, Any]:
    """ documentation already in module """
    if key in dct:
        return dct[key]
    else:
        return default
