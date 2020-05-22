#! /usr/bin/env python3

# Import the os module to work with files and directories.
import os

# Store the path to where the FASTA files for the GreenGenees 16S Reference Database are located to a variable.
directory = "/home/unhTW/share/mcbs913_2020/addiction/16S_Reference_Files/Reference_FASTA"

# Use a try block with an except statement to manipulate files and to detect any errors that may arise when working with the files.
try:
    # Iterate through each file in the directory storing a specific path.
    # Work with the specific GreenGenes FASTA file, and open the file to read through its contents.
    # Open a new file as well to write the starting positions of specified primer sequences as output.
    for file in os.listdir(directory):
        if file.endswith("GreenGenes.fasta"):
            with open(file, "r") as input:
                with open("GreenGenes_Forward_Primer_Starting_Position.txt", "w") as output:
                    # Iterate through each line of the input file.
                    for line in input:
                        # Store each variation of the primer sequence in separate variables.
                        # Note: Variations of primer sequences take into account ambiguous nucleotides having the possibility of being an A, G, T, or C depending on the letter designation.
                        variation_1 = "GTGCCAGCAGCCGCGGTAA"
                        variation_2 = "GTGCCAGCCGCCGCGGTAA"
                        variation_3 = "GTGTCAGCAGCCGCGGTAA"
                        variation_4 = "GTGTCAGCCGCCGCGGTAA"
                        # Note: The reverse complement of each primer sequence variation is also taken into account.
                        variation_5 = "TTACCGCGGCTGCTGGCAC"
                        variation_6 = "TTACCGCGGCGGCTGGCAC"
                        variation_7 = "TTACCGCGGCTGCTGACAC"
                        variation_8 = "TTACCGCGGCGGCTGACAC"
                        # Write out each unique header to the output file.
                        if ">" in line:
                            output.write("Header: {0}".format(line))
                        # Use if statements to detect the presence of each primer sequence variation in each 16S reference sequence and write out the starting position number into the output file.
                        if variation_1 in line:
                            position = line.find(variation_1)
                            output.write("Starting Position: {0}\n".format(position))
                            output.write("\n")
                        if variation_2 in line:
                            position = line.find(variation_2)
                            output.write("Starting Position: {0}\n".format(position))
                            output.write("\n")
                        if variation_3 in line:
                            position = line.find(variation_3)
                            output.write("Starting Position: {0}\n".format(position))
                            output.write("\n")
                        if variation_4 in line:
                            position = line.find(variation_4)
                            output.write("Starting Position: {0}\n".format(position))
                            output.write("\n")
                        if variation_5 in line:
                            position = line.find(variation_5)
                            output.write("Starting Position: {0}\n".format(position))
                            output.write("\n")
                        if variation_6 in line:
                            position = line.find(variation_6)
                            output.write("Starting Position: {0}\n".format(position))
                            output.write("\n")
                        if variation_7 in line:
                            position = line.find(variation_7)
                            output.write("Starting Position: {0}\n".format(position))
                            output.write("\n")
                        if variation_8 in line:
                            position = line.find(variation_8)
                            output.write("Starting Position: {0}\n".format(position))
                            output.write("\n")
except IOError:
    print("An error has occurred")
