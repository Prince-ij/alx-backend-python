#!/usr/bin/env python3
"""
Module name: 6-sum_mixed_list
function: sum_mixed_list
Description: sums a list of floats and ints
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: Union[List[float], List[int]]) -> float:
    """ look at the module docs
    """
    total: float = 0
    for i in mxd_lst:
        total += i
    return total
