#!/usr/bin/env python3
"""
Yet another complicated type annotations
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    This creates a tuple, dont expect all
    those complicated docs which are boring,
    I dont need to tell the return type or
    variables, look them yourself
    """
    return (k, float(v**2))
