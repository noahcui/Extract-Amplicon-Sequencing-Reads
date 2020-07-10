#! /usr/bin/env python3

import os
import sys
import re
from collections import OrderedDict
import collections

Set = set()
total = 0
Dict = {}

with open(str(sys.argv[1]), "r") as input:
    for line in input:
        fields = line.split("\t")
        if "Count" in fields[0]:
            continue
        if len(fields)< 7:
            continue
        if float(fields[2])>= 50 and float(fields[3])== 60:
            COUNT = fields[0]
            Abundance = fields[1]
            avgQ = fields[2]
            Target = fields[6]
            total += int(COUNT)
            if Target in Dict:
                Dict[Target] += int(COUNT)
            else:
                Dict.update( {Target : int(COUNT)} )
                    #print(total)


                        #print(reference_name,dict[reference_name]+"\n")

sorted_dict = sorted(Dict.items(), key=lambda kv: kv[1])
dict_ret = collections.OrderedDict(sorted_dict)
print(dict_ret)
print("\n", total)