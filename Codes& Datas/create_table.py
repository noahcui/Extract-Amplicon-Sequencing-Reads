#!/usr/bin/python

import sys
import sqlite3

def create_table_fasta(c, table_name):
    cmd = "create table fasta(Reference text,\
        Query text,\
        primary key(Reference));"
    c.execute(cmd)
    print("table created successfully, now inserting datas")

def create_table_pos(c, table_name):
    cmd = "create table " + table_name + "(Header text,\
        start_POS int);"
    c.execute(cmd)
    print("table created successfully, now inserting datas")

def create_table_sam(c, table_name):
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
        TAG text,\
        FILE text\
        primary key(QNAME, POS, FLAG, FILE));"
    c.execute(cmd)
    print("table created successfully, now inserting datas")


if __name__ == '__main__':
    file_name = "Silva.fasta"
    conn = None
    dbname = sys.argv[1]
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    create_table_fasta(c, "fasta")
    create_table_sam(c, 'sam')
    create_table_pos(c, 'startPOS')
    conn.commit()
    conn.close()