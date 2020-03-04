#!/usr/bin/python

# put it in the same directory where sam files are. 
# cmd: generate_DB.py DBname tablename1 tablename2... where table name is the name of sam files without ".sam"


import sys
import sqlite3



def create_table(table_name):
    cmd = "create table " + table_name + "(QNAME text,\
        FLAG int,\
        RENAME text,\
        POS int,\
        MAPQ int,\
        CIGAR text,\
        RNEXT text,\
        PNEXT int,\
        TLEN int,\
        SEQ text,\
        QUAL text,\
        primary key(QNAME, POS));"
    print("files oppened successfully, now creating tables")
    c.execute(cmd)

def insert_data(table_name, data):
    cmd = "insert into " + table_name + "(QNAME, FLAG, RENAME, POS, MAPQ, CIGAR, RNEXT, PNEXT, TELEN, SEQ, QUAL)\
        values(" + data + ")"
    c.execute(cmd)
        
if __name__ == '__main__':
    conn = sqlite3.connect(sys.argv[0])
    c= conn.cursor()
    for i in range(len(sys.argv)):
        if i > 0:
            table_name = sys.argv[i]
            create_table(table_name)
            file_name = table_name+".sam"
            with open(file_name, "r") as sam_file:
                for line in sam_file:
                    fields = line.split("\t")
                    if "@" not in fields[0]:
                        for i in range(len(fields)):
                            data = data + fields[i] + ", " 
                        data = data - ","
                        insert_data(table_name, data)
            
