#!/bin/bash

echo "run bwa:"

bwa mem  /home/unhTW/share/mcbs913_2020/addiction/16S_Reference_Files/$1  /home/unhTW/share/mcbs913_2020/addiction/Metagenomic_Dataset/$2  /home/unhTW/share/mcbs913_2020/addiction/Metagenomic_Dataset/$3 >>  /home/unhTW/share/mcbs913_2020/addiction/$4.sam