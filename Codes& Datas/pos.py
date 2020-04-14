#!/usr/bin/python

import sys
import sqlite3

def create_table(c, table_name):
    cmd = "create table " + table_name + "(File text,\
        Query text,\
        Reference text,\
        Position int);"
    c.execute(cmd)
    print("table created successfully, now inserting datas")

def insert_data(c, table_name, data):
    cmd = "INSERT INTO " + table_name + "(File, Query, Reference, Position) VALUES (?,?,?,?);"
    c.execute(cmd, data)

if __name__ == '__main__':
    conn = None
    dbname = sys.argv[1]
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    table_name = "startPOS"
    create_table(c, table_name)
    for i in range(len(sys.argv)):
        if i > 1:
            #directiory
            file_name = sys.argv[i]
            count = -1
            with open(file_name, "r") as pos_file:
                for line in pos_file:
                    count = count + 1
                    if count % 5 == 0:
                        File = line.replace('File: ', '')
                    if count % 5 == 1:
                        Query = line.replace('Query: ', '')
                    if count % 5 == 2:
                        Reference = line.replace('Reference: ', '')
                    if count % 5 == 3:
                        Position = line.replace('Position: ', '')
                    else:
                        data = (File, Query, Reference, Position)
                        insert_data(c, table_name, data)
                    
    conn.commit()
    conn.close()