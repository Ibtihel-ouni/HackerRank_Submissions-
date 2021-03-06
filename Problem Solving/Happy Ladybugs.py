#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
from itertools import groupby

# Complete the happyLadybugs function below.
def happyLadybugs(b):
    
    c = Counter(b)
    if "_" in c:
        for x,y in c.items():
            if y < 2 and x != "_":
                return "NO"
    else:
        for x,y in groupby(b):
            if len(list(y)) < 2:
                return "NO"
    return "YES"
