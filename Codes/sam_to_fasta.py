#! /usr/bin/env python3

import os

# Set a variable to the path of the directory for the files you wish to access. 
directory = "/home/unhTW/share/mcbs913_2020/addiction/16S_Reference_Files/BWA_Alignments/Quality_Filtered_Alignments"

# Surround the code with a try block to detect if there are any issues with opening files.
try:
    # Iterate over each file in the directory.
    for file in os.listdir(directory):
        # Work only with files of a specific format.
        if file.endswith(".sam"):
            # Split the filename by an underscore delimiter, and set the first column as the standard name for the output file.
            filename = file.split("_")
            output_name = filename[0]
            # Use with statements to read input files and write output files.
            with open(file, "r") as input:
                with open("{0}.fa".format(output_name), "w") as output:
                    # Iterate over each line in the input file, and split each line by a tab delimiter.
                    for line in input:
                        fields = line.split("\t")
                        # Set the query name, reference name, and sequence to their own variables.
                        query_name = fields[0]
                        reference_name = fields[2]
                        sequence = fields[9]
                        # Write out the lines from each input file in the standard FASTA file format in the output file. 
                        output.write(">{0}-{1}\n".format(query_name, reference_name))
                        output.write("{0}\n".format(sequence))
except IOError:
    print("An error has occurred.")

