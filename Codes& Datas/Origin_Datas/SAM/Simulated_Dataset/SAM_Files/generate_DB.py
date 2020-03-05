#!/usr/bin/python

# put this script in the same directory where sam files are. 
# cmd: generate_DB.py DBname tablename1 tablename2... where table name is the name of sam files without ".sam"


import sys
import sqlite3



def create_table(c, table_name):
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
    c.execute(cmd)
    print("table created successfully, now inserting datas")

def insert_data(c, table_name, data):
    cmd = "INSERT INTO " + table_name + "(QNAME, FLAG, RENAME, POS, MAPQ, CIGAR, RNEXT, PNEXT, TLEN, SEQ, QUAL) VALUES (?,?,?,?,?,?,?,?,?,?,?);"
    c.execute(cmd, data)
        
if __name__ == '__main__':
    conn = None
    dbname = sys.argv[1]
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    print("files oppened successfully, now creating tables")
    for i in range(len(sys.argv)):
        if i > 1:
            table_name = sys.argv[i]
            create_table(c, table_name)
            file_name = table_name+".sam"
            with open(file_name, "r") as sam_file:
                for line in sam_file:
                    fields = line.split("\t")
                    if "@" not in fields[0]:
                        QNAME = fields[0]
                        FLAG = fields[1]
                        RENAME = fields[2]
                        POS = fields[3]
                        MAPQ = fields[4]
                        CIGAR = fields[5]
                        RNEXT = fields[6]
                        PNEXT = fields[7]
                        TLEN = fields[8]
                        SEQ = fields[9]
                        QUAL = fields[10]
                        data = (QNAME, FLAG, RENAME, POS, MAPQ, CIGAR, RNEXT, PNEXT, TLEN, SEQ, QUAL)
                        insert_data(c, table_name, data)
    
    conn.commit()
    conn.close()
            
