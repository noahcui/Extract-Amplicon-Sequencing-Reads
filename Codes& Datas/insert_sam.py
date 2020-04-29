#!/usr/bin/python

# put this script in the same directory where sam files are. 
# cmd: generate_DB.py DBname tablename1 tablename2... where table name is the name of sam files
# The DBname should be DBname.db, This script only create a new database, can't dealing with a database that already exists.

import sys
import sqlite3



def create_table(c, table_name):
    cmd = "create table " + table_name + "(QNAME text,\
        FLAG int,\
        REFNAME text,\
        POS int,\
        MAPQ int,\
        CIGAR text,\
        RNEXT text,\
        PNEXT int,\
        TLEN int,\
        SEQ text,\
        QUAL text,\
        TAG text,\
        FILE text\
        primary key(QNAME, NUM));"
    c.execute(cmd)
    print("table created successfully, now inserting datas")

def create_header(c, table_name):
    cmd = "create table " + table_name + "(FILE text, HEADER text)"
    c.execute(cmd)
    print("header table created successfully, now inserting datas")

def insert_headers(c, table_name, data):
    cmd = "INSERT INTO " + table_name + "(FILE, HEADER) VALUES(?,?);"
    c.execute(cmd, data)

def insert_data(c, table_name, data):
    cmd = "INSERT INTO " + table_name + "(QNAME, NUM, FLAG, REFNAME, POS, MAPQ, CIGAR, RNEXT, PNEXT, TLEN, SEQ, QUAL, TAG, FILE) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?);"
    c.execute(cmd, data)
        
if __name__ == '__main__':
    conn = None
    dbname = sys.argv[1]
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    print("files oppened successfully, now creating tables")
    dict = {}
    for i in range(len(sys.argv)):
        if i > 1:
            table_name = sys.argv[i]
            file_name = table_name
            print("file writing: ", file_name)
            with open(file_name, "r") as sam_file:
                for line in sam_file:
                    fields = line.split("\t")
                    if "@" not in fields[0]:
                        QNAME = fields[0]
                        FLAG = fields[1]
                        REFNAME = fields[2]
                        POS = fields[3]
                        MAPQ = fields[4]
                        CIGAR = fields[5]
                        RNEXT = fields[6]
                        PNEXT = fields[7]
                        TLEN = fields[8]
                        SEQ = fields[9]
                        QUAL = fields[10]
                        TAG= fields[11]
                        for n in range(12, len(fields)):
                            TAG = TAG + ('\t') + fields[n]
                            n = n + 1

                        if QNAME in dict:
                            dict[QNAME] = dict[QNAME] + 1
                            NUM = dict[QNAME]
                        else:
                            dict[QNAME] = 0
                            NUM = 0
                        
                        data = (QNAME, NUM, FLAG, REFNAME, POS, MAPQ, CIGAR, RNEXT, PNEXT, TLEN, SEQ, QUAL, TAG, file_name)
                        #if FLAG & 4 != 4:
                        insert_data(c, 'sam', data)
    
    conn.commit()
    conn.close()
            
