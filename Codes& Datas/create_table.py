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
    cmd = "create table " + table_name + "(File text,\
        Query text,\
        Reference text,\
        Position int);"
    c.execute(cmd)
    print("table created successfully, now inserting datas")

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
        INFO text,\
        FILE text);"
    c.execute(cmd)
    print("table created successfully, now inserting datas")


if __name__ == '__main__':
    file_name = "Silva.fasta"
    conn = None
    dbname = sys.argv[1]
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    create_table_fasta(c, "fasta")
    create_table(c, 'sam')
    create_table(c, 'startPOS')
    conn.commit()
    conn.close()