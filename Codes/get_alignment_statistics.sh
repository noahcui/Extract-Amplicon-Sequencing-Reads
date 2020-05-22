#! /usr/bin/env bash

# Set a variable to the location where all of the SAM files are.
directory=/home/unhTW/share/mcbs913_2020/addiction/16S_Reference_Files/BWA_Alignments/*

# Iterate through each file in the directory where all of the SAM files are.
# For each file that is iterated through in the directory, append the file name into a text file.
# Additionally, after the name of the file has been appended, use "samtools flagstat" to retrieve statistics for each file.
for file in $directory
do
    echo $file >> BWA_Flag_Statistics.txt
    samtools flagstat $file >> BWA_Flag_Statistics.txt
done
