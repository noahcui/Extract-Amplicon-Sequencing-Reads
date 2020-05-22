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
                with open("GreenGenes_Reverse_Primer_Starting_Position.txt", "w") as output:
                    # Iterate through each line of the input file.
                    for line in input:
                        # Store each variation of the primer sequence in separate variables.
                        # Note: Variations of primer sequences take into account ambiguous nucleotides having the possibility of being an A, G, T, or C depending on the letter designation.
                        variation_1 = "ATTAGATACCCTGGTAGTCC"
                        variation_2 = "ATTAGATACCCGCGTAGTCC"
                        variation_3 = "ATTAGATACCCCTGTAGTCC"
                        variation_4 = "ATTAGATACCCTAGTAGTCC"
                        variation_5 = "ATTAGATACCCGGGTAGTCC"
                        variation_6 = "ATTAGATACCCCCGTAGTCC"
                        variation_7 = "ATTAGATACCCTTGTAGTCC"
                        variation_8 = "ATTAGATACCCGAGTAGTCC"
                        variation_9 = "ATTAGATACCCCGGTAGTCC"
                        variation_10 = "ATTAGATACCCTCGTAGTCC"
                        variation_11 = "ATTAGATACCCGTGTAGTCC"
                        variation_12 = "ATTAGATACCCCAGTAGTCC"
                        variation_13 = "ATTAGAAACCCTGGTAGTCC"
                        variation_14 = "ATTAGAAACCCGCGTAGTCC"
                        variation_15 = "ATTAGAAACCCCTGTAGTCC"
                        variation_16 = "ATTAGAAACCCTAGTAGTCC"
                        variation_17 = "ATTAGAAACCCGGGTAGTCC"
                        variation_18 = "ATTAGAAACCCCCGTAGTCC"
                        variation_19 = "ATTAGAAACCCTTGTAGTCC"
                        variation_20 = "ATTAGAAACCCGAGTAGTCC"
                        variation_21 = "ATTAGAAACCCCGGTAGTCC"
                        variation_22 = "ATTAGAAACCCTCGTAGTCC"
                        variation_23 = "ATTAGAAACCCGTGTAGTCC"
                        variation_24 = "ATTAGAAACCCCAGTAGTCC"
                        # Note: The reverse complement of each primer sequence variation is also taken into account.
                        variation_25 = "GGACTACCAGGGTATCTAAT"
                        variation_26 = "GGACTACGCGGGTATCTAAT"
                        variation_27 = "GGACTACAGGGGTATCTAAT"
                        variation_28 = "GGACTACTAGGGTATCTAAT"
                        variation_29 = "GGACTACCCGGGTATCTAAT"
                        variation_30 = "GGACTACGGGGGTATCTAAT"
                        variation_31 = "GGACTACAAGGGTATCTAAT"
                        variation_32 = "GGACTACTCGGGTATCTAAT"
                        variation_33 = "GGACTACCGGGGTATCTAAT"
                        variation_34 = "GGACTACGAGGGTATCTAAT"
                        variation_35 = "GGACTACACGGGTATCTAAT"
                        variation_36 = "GGACTACTGGGGTATCTAAT"
                        variation_37 = "GGACTACCAGGGTTTCTAAT"
                        variation_38 = "GGACTACGCGGGTTTCTAAT"
                        variation_39 = "GGACTACAGGGGTTTCTAAT"
                        variation_40 = "GGACTACTAGGGTTTCTAAT"
                        variation_41 = "GGACTACCCGGGTTTCTAAT"
                        variation_42 = "GGACTACGGGGGTTTCTAAT"
                        variation_43 = "GGACTACAAGGGTTTCTAAT"
                        variation_44 = "GGACTACTCGGGTTTCTAAT"
                        variation_45 = "GGACTACCGGGGTTTCTAAT"
                        variation_46 = "GGACTACGAGGGTTTCTAAT"
                        variation_47 = "GGACTACACGGGTTTCTAAT"
                        variation_48 = "GGACTACTGGGGTTTCTAAT"
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
                        if variation_9 in line:
                            position = line.find(variation_9)
                            output.write("Starting Position: {0}\n".format(position))
                            output.write("\n")
                        if variation_10 in line:
                            position = line.find(variation_10)
                            output.write("Starting Position: {0}\n".format(position))
                            output.write("\n")
                        if variation_11 in line:
                            position = line.find(variation_11)
                            output.write("Starting Position: {0}\n".format(position))
                            output.write("\n")
                        if variation_12 in line:
                            position = line.find(variation_12)
                            output.write("Starting Position: {0}\n".format(position))
                            output.write("\n")
                        if variation_13 in line:
                            position = line.find(variation_13)
                            output.write("Starting Position: {0}\n".format(position))
                            output.write("\n")
                        if variation_14 in line:
                            position = line.find(variation_14)
                            output.write("Starting Position: {0}\n".format(position))
                            output.write("\n")
                        if variation_15 in line:
                            position = line.find(variation_15)
                            output.write("Starting Position: {0}\n".format(position))
                            output.write("\n")
                        if variation_16 in line:
                            position = line.find(variation_16)
                            output.write("Starting Position: {0}\n".format(position))
                            output.write("\n")
                        if variation_17 in line:
                            position = line.find(variation_17)
                            output.write("Starting Position: {0}\n".format(position))
                            output.write("\n")
                        if variation_18 in line:
                            position = line.find(variation_18)
                            output.write("Starting Position: {0}\n".format(position))
                            output.write("\n")
                        if variation_19 in line:
                            position = line.find(variation_19)
                            output.write("Starting Position: {0}\n".format(position))
                            output.write("\n")
                        if variation_20 in line:
                            position = line.find(variation_20)
                            output.write("Starting Position: {0}\n".format(position))
                            output.write("\n")
                        if variation_21 in line:
                            position = line.find(variation_21)
                            output.write("Starting Position: {0}\n".format(position))
                            output.write("\n")
                        if variation_22 in line:
                            position = line.find(variation_22)
                            output.write("Starting Position: {0}\n".format(position))
                            output.write("\n")
                        if variation_23 in line:
                            position = line.find(variation_23)
                            output.write("Starting Position: {0}\n".format(position))
                            output.write("\n")
                        if variation_24 in line:
                            position = line.find(variation_24)
                            output.write("Starting Position: {0}\n".format(position))
                            output.write("\n")
                        if variation_25 in line:
                            position = line.find(variation_25)
                            output.write("Starting Position: {0}\n".format(position))
                            output.write("\n")
                        if variation_26 in line:
                            position = line.find(variation_26)
                            output.write("Starting Position: {0}\n".format(position))
                            output.write("\n")
                        if variation_27 in line:
                            position = line.find(variation_27)
                            output.write("Starting Position: {0}\n".format(position))
                            output.write("\n")
                        if variation_28 in line:
                            position = line.find(variation_28)
                            output.write("Starting Position: {0}\n".format(position))
                            output.write("\n")
                        if variation_29 in line:
                            position = line.find(variation_29)
                            output.write("Starting Position: {0}\n".format(position))
                            output.write("\n")
                        if variation_30 in line:
                            position = line.find(variation_30)
                            output.write("Starting Position: {0}\n".format(position))
                            output.write("\n")
                        if variation_31 in line:
                            position = line.find(variation_31)
                            output.write("Starting Position: {0}\n".format(position))
                            output.write("\n")
                        if variation_32 in line:
                            position = line.find(variation_32)
                            output.write("Starting Position: {0}\n".format(position))
                            output.write("\n")
                        if variation_33 in line:
                            position = line.find(variation_33)
                            output.write("Starting Position: {0}\n".format(position))
                            output.write("\n")
                        if variation_34 in line:
                            position = line.find(variation_34)
                            output.write("Starting Position: {0}\n".format(position))
                            output.write("\n")
                        if variation_35 in line:
                            position = line.find(variation_35)
                            output.write("Starting Position: {0}\n".format(position))
                            output.write("\n")
                        if variation_36 in line:
                            position = line.find(variation_36)
                            output.write("Starting Position: {0}\n".format(position))
                            output.write("\n")
                        if variation_37 in line:
                            position = line.find(variation_37)
                            output.write("Starting Position: {0}\n".format(position))
                            output.write("\n")
                        if variation_38 in line:
                            position = line.find(variation_38)
                            output.write("Starting Position: {0}\n".format(position))
                            output.write("\n")
                        if variation_39 in line:
                            position = line.find(variation_39)
                            output.write("Starting Position: {0}\n".format(position))
                            output.write("\n")
                        if variation_40 in line:
                            position = line.find(variation_40)
                            output.write("Starting Position: {0}\n".format(position))
                            output.write("\n")
                        if variation_41 in line:
                            position = line.find(variation_41)
                            output.write("Starting Position: {0}\n".format(position))
                            output.write("\n")
                        if variation_42 in line:
                            position = line.find(variation_42)
                            output.write("Starting Position: {0}\n".format(position))
                            output.write("\n")
                        if variation_43 in line:
                            position = line.find(variation_43)
                            output.write("Starting Position: {0}\n".format(position))
                            output.write("\n")
                        if variation_44 in line:
                            position = line.find(variation_44)
                            output.write("Starting Position: {0}\n".format(position))
                            output.write("\n")
                        if variation_45 in line:
                            position = line.find(variation_45)
                            output.write("Starting Position: {0}\n".format(position))
                            output.write("\n")
                        if variation_46 in line:
                            position = line.find(variation_46)
                            output.write("Starting Position: {0}\n".format(position))
                            output.write("\n")
                        if variation_47 in line:
                            position = line.find(variation_47)
                            output.write("Starting Position: {0}\n".format(position))
                            output.write("\n")
                        if variation_48 in line:
                            position = line.find(variation_48)
                            output.write("Starting Position: {0}\n".format(position))
                            output.write("\n")
except IOError:
    print("An error has occurred")
