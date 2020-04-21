#!/usr/bin/python

import sys
import sqlite3

def create_table(c, table_name):
    cmd = "create table " + table_name + "(Header text,\
        start_POS int);"
    c.execute(cmd)
    print("table created successfully, now inserting datas")

def insert_data(c, table_name, data):
    cmd = "INSERT INTO " + table_name + "(Header, Start_POS) VALUES (?,?);"
    c.execute(cmd, data)

if __name__ == '__main__':
    conn = None
    dbname = sys.argv[1]
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    table_name = "startPOS"
    for i in range(len(sys.argv)):
        if i > 1:
            #directiory
            file_name = sys.argv[i]
            print("file: ", file_name)
            with open(file_name, "r") as pos_file:
                for line in pos_file:
                    h = False
                    fields = line.split(" ")
                    if h:
                        if 'Starting' in line:
                            POS = fields[2].replace('\n')
                            h = False
                            data = (Header, pos)
                            insert_data(c, table_name, data)
                        else:
                            pos = -1
                            h = False
                            data = (Header, pos)
                            insert_data(c, table_name, data)
                            if 'header' in line:
                                h = True
                                Header = fields[1].replace('>','')
                    else:
                        if 'header' in line:
                            h = True
                            Header = fields[1].replace('>','')
                    
    conn.commit()
    conn.close()