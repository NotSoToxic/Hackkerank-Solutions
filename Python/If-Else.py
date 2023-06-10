import math
import os
import random
import re
import sys

def random(n):
    if n%2==1 or 6<=n<=20:
        print("Random!")
    else:
        print("Not Random!")

random(int(input()))