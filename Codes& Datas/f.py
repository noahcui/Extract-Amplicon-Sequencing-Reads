#!/usr/bin/python

import sys
import sqlite3


def create_table(c, table_name):
    cmd = "create or replace table fasta (Reference,text\
        Query, text);"
    c.execute(cmd)
    print("table created successfully, now inserting datas")


def insert_data(c, table_name, data):
    cmd = "INSERT INTO " + table_name + \
        "(INFO, SEQ, START, END) VALUES (?,?,?,?);"
    c.execute(cmd, data)


if __name__ == '__main__':
    file_name = "Silva.fasta"
    conn = None
    dbname = sys.argv[1]
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    Query = ''
    with open(file_name, "r") as pos_file:
        for line in pos_file:
            fields = line.split(" ")
            if '>'in line:
                if Query != '':
                    data = (Reference, Query)
                    insert_data(c, "fasta", data)
                    Query = ''
                Reference = fields[0].replace('>','')
            else:
                Query = Query + line.replace('\n','')
        data = (Reference, Query)
        insert_data(c, "fasta", data)
    conn.commit()
    conn.close()