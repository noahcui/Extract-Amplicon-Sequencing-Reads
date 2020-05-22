#!/usr/bin/python

import sys
import sqlite3

if __name__ == '__main__':
    for i in range(len(sys.argv)):
        file_name = sys.argv[i]
        with open(file_name, "r") as pos_file:
            for line in pos_file:
                if '@PG' in line:
                    if line.count('.gz') > 1:
                        print("yes", file_name, line)
                    else:
                        print("no", file_name, line)