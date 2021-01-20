import numpy as np
import pandas as pd
import math
import copy

# Utility function to check if an array/list is sorted


def IsSorted(Array):
    """Boolean output, checks to see if an array is sorted."""
    length = len(Array)
    assert length > 0, "Array empty"

    lastElement = - float("inf")
    for element in Array:
        if element < lastElement:
            return False
        lastElement = element
    return True

# Code block by Movsisyan
