#! /usr/bin/env python3

# Import the os module to work with files and directories.
import os

# Store the path to where the FASTA files for the Silva 16S Reference Database are located to a variable.
directory = "/home/unhTW/share/mcbs913_2020/addiction/16S_Reference_Files/Reference_FASTA"

# Use a try block with an except statement to manipulate files and to detect any errors that may arise when working with the files.
try:
    # Iterate through each file in the directory storing a specific path.
    # Work with the specific GreenGenes FASTA file, and open the file to read through its contents.
    # Open a new file as well to write the starting positions of specified primer sequences as output.
    for file in os.listdir(directory):
        if file.endswith("Silva_Updated.fasta"):
            with open(file, "r") as input:
                with open("Silva_Reverse_Primer_Starting_Position.txt", "w") as output:
                    # Iterate through each line of the input file.
                    for line in input:
                        # Store each variation of the primer sequence in separate variables.
                        # Note: Variations of primer sequences take into account ambiguous nucleotides having the possibility of being an A, G, T, or C depending on the letter designation.
                        # Note: Since the Silva 16S Reference Database sequences are RNA, all of the T's of the primer DNA sequences were changed to U's.
                        variation_1 = "AUUAGAUACCCUGGUAG"
                        variation_2 = "AUUAGAUACCCGCGUAG"
                        variation_3 = "AUUAGAUACCCCUGUAG"
                        variation_4 = "AUUAGAUACCCUAGUAG"
                        variation_5 = "AUUAGAUACCCGGGUAG"
                        variation_6 = "AUUAGAUACCCCCGUAG"
                        variation_7 = "AUUAGAUACCCUUGUAG"
                        variation_8 = "AUUAGAUACCCGAGUAG"
                        variation_9 = "AUUAGAUACCCCGGUAG"
                        variation_10 = "AUUAGAUACCCUCGUAG"
                        variation_11 = "AUUAGAUACCCGUGUAG"
                        variation_12 = "AUUAGAUACCCCAGUAG"
                        variation_13 = "AUUAGAAACCCUGGUAG"
                        variation_14 = "AUUAGAAACCCGCGUAG"
                        variation_15 = "AUUAGAAACCCCUGUAG"
                        variation_16 = "AUUAGAAACCCUAGUAG"
                        variation_17 = "AUUAGAAACCCGGGUAG"
                        variation_18 = "AUUAGAAACCCCCGUAG"
                        variation_19 = "AUUAGAAACCCUUGUAG"
                        variation_20 = "AUUAGAAACCCGAGUAG"
                        variation_21 = "AUUAGAAACCCCGGUAG"
                        variation_22 = "AUUAGAAACCCUCGUAG"
                        variation_23 = "AUUAGAAACCCGUGUAG"
                        variation_24 = "AUUAGAAACCCCAGUAG"
                        # Note: The reverse complement of each primer sequence variation is also taken into account.
                        variation_25 = "CUACCAGGGUAUCUAAU"
                        variation_26 = "CUACGCGGGUAUCUAAU"
                        variation_27 = "CUACAGGGGUAUCUAAU"
                        variation_28 = "CUACUAGGGUAUCUAAU"
                        variation_29 = "CUACCCGGGUAUCUAAU"
                        variation_30 = "CUACGGGGGUAUCUAAU"
                        variation_31 = "CUACAAGGGUAUCUAAU"
                        variation_32 = "CUACUCGGGUAUCUAAU"
                        variation_33 = "CUACCGGGGUAUCUAAU"
                        variation_34 = "CUACGAGGGUAUCUAAU"
                        variation_35 = "CUACACGGGUAUCUAAU"
                        variation_36 = "CUACUGGGGUAUCUAAU"
                        variation_37 = "CUACCAGGGUUUCUAAU"
                        variation_38 = "CUACGCGGGUUUCUAAU"
                        variation_39 = "CUACAGGGGUUUCUAAU"
                        variation_40 = "CUACUAGGGUUUCUAAU"
                        variation_41 = "CUACCCGGGUUUCUAAU"
                        variation_42 = "CUACGGGGGUUUCUAAU"
                        variation_43 = "CUACAAGGGUUUCUAAU"
                        variation_44 = "CUACUCGGGUUUCUAAU"
                        variation_45 = "CUACCGGGGUUUCUAAU"
                        variation_46 = "CUACGAGGGUUUCUAAU"
                        variation_47 = "CUACACGGGUUUCUAAU"
                        variation_48 = "CUACUGGGGUUUCUAAU"
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
