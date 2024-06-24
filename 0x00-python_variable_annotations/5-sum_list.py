#!/usr/bin/env python3
"""
A function to sum lists
blah blah blah, It should be annotated
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Sums up values in a list
    """
    sum: float = 0
    for i in input_list:
        sum += i
    return sum
