#!/usr/bin/env python3
"""
Write a type-annotated function make_multiplier
that takes a float multiplier as argument and
returns a function that multiplies a float by
multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ the outer function """
    def multiply(x: float) -> float:
        """ the inner function """
        return x * multiplier
    return multiply
