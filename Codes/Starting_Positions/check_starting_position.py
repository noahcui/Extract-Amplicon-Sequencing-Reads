#! /usr/bin/env python3

import os

directory = "/home/unhTW/share/mcbs913_2020/addiction/bwa_results/Public/Quality_Filtered"

try:
    for file in os.listdir(directory):
        if file.endswith(".sam"):
            with open(file, "r") as input:
                with open("Starting_Positions.txt", "w") as output:
                    for line in input:
                        fields = line.split("\t")
                        #query_name = fields[0]
                        #reference_name = fields[2]
                        starting_position = fields[3]
                        #output.write("File: {0}\n".format(file))
                        #output.write("Query: {0}\n".format(query_name))
                        #output.write("Reference: {0}\n".format(reference_name))
                        output.write("{0}\n".format(starting_position))
                        #output.write("\n")
except IOError:
    print("An error has occurred")
