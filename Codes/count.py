#! /usr/bin/env python3

import os
import sys
import re


total = 0


with open(str(sys.argv[1]), "r") as input:
    for line in input:
        fields = line.split("\t")
            if "@" not in fields[0]:
                total += 1
                    









