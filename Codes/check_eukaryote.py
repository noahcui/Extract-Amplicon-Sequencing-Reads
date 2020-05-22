#! /usr/bin/env python3

import os
import sys
import re

directory = "/home/unhTW/share/mcbs913_2020/addiction/bwa_results/Simulate/Other"
directory2 = "/home/unhTW/share/mcbs913_2020/addiction/16S_Reference_Files/Reference_FASTA"

dict = {}
counter = 0
total = 0

for file in os.listdir(directory2):
    with open("/home/unhTW/share/mcbs913_2020/addiction/16S_Reference_Files/Reference_FASTA/Silva.fasta", "r") as input:
            for line in input:
                if line[0] != ">" :
                    continue
                fields = line.replace(">"," ").replace(";"," ").split()
                one = fields[0]
                two = fields[1]
                dict.update( {one : two} )




try:
    for file in os.listdir(directory):
        with open(str(sys.argv[1]), "r") as input:
            for line in input:
                fields = line.split("\t")
                if "@" not in fields[0]:
                    QNAME = fields[0]
                    FLAG = fields[1]
                    reference_name = fields[2]
                    CIAGR = fields[5]
                    #starting_position = fields[3]
                    #output.write("File: {0}\n".format(file))
                    #output.write("Query: {0}\n".format(query_name))
                    #output.write("Reference: {0}\n".format(reference_name))
                    #output.write("{0}\n".format(reference_name))
                    #output.write("\n")

                    total += 1
                    #print(total)
                    pattern = "S(.*?)M"
                    mvalue = re.search(pattern, CIAGR)
                    if mvalue:
                        mvalue = mvalue.group(1)
                        print(CIAGR)
                        print("M:  ",mvalue)
                    #print(CIAGR)
                    if reference_name != "*":
                        val = dict[reference_name]
                        if val == "Eukaryota" :
                            if mvalue>=100:
                                counter+=1

                        #print(reference_name,dict[reference_name]+"\n")










except IOError:
    print("An error has occurred")
print(counter,"/",total)
f = open(str(sys.argv[2]), "w")
ret = sys.argv[2]+":"+str(counter)+"/"+str(total)
f.write(ret)
f.close()
