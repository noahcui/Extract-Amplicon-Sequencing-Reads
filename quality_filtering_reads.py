#! /usr/bin/env python3

import os

directory = "/home/unhTW/share/mcbs913_2020/addiction/16S_Reference_Files/BWA_Alignments"

# Surround code with a try block to determine if any errors occur with opening files. 
try:
    for file in os.listdir(directory):
        if file.endswith(".sam"):
            # Use with statements to read input files and write output files.
            with open(file, "r") as input:
                with open("{0}_QualityFiltered.sam".format(file), "w") as output:
                    # For each input file, iterate through each line and split the elements by a tab delimiter to generate separate columns ("fields").
                    for line in input:
                        fields = line.split("\t")
                        # Use branching to filter through the data for the high quality reads spanning a specific variable region of the 16S rRNA gene:
                        # 1. Remove any lines that begin with "@" (typically found at the top of the SAM file)
                        # 2. Remove any reads that were not mapped (designated by a 4).
                        # 3. Remove any reads that has a mapping quality below 50.
                        # 4. Remove any reads that do not span the V4 region of the 16S rRNA gene (designated by commonly used forward and reverse primers to generate an amplicon).
                        if "@" not in fields[0] and fields[1] != "4":
                            if int(fields[4]) >= 50:
                                if int(fields[3]) >= 515 and int(fields[3]) <= 806:
                                    # Write lines that passed the filters to a new output file.
                                    output.write(line)
except IOError:
    print("An error has occurred.")
