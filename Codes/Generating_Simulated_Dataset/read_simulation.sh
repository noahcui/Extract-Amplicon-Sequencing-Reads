#! /usr/bin/env bash

# This script is meant to generate a simulated read dataset of known referene genomes using ART.
# The public dataset we are using is Illumina paired-end metagenomic reads generated using the HiSeq 4000 (2 x 150bp).

# The "art_illumina" command is used to simulate paired-end reads off of an Illumina sequencing platform using the following parameters:
    # 1. "-sam": A SAM alignment file is generated for each reference organism
    # 2. "-i": Input reference FASTA file of select whole genomes
    # 3. "-p": Indicates paired-end sequencing simulation mode
    # 4. "-l": Length of each read
    # 5. "-f": Fold coverage
    # 6. "m": Mean length of each read
    # 7. "-s": Standard deviation of each read
    # 8. "-o": Output file name

art_illumina -sam -i Reference_Genomes.fasta -p -l 150 -f 50 -m 200 -s 10 -o Reference_Genomes_Paired



