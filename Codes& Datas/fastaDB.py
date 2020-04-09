#!/usr/bin/python

import sys
import sqlite3

def create_table(c, table_name):
    cmd = "create or replace table " + table_name + "(INFO,text\
        SEQ text,\
        START int,\
        END int);"
    c.execute(cmd)
    print("table created successfully, now inserting datas")

def insert_data(c, table_name, data):
    cmd = "INSERT INTO " + table_name + "(INFO, SEQ, START, END) VALUES (?,?,?,?);"
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
            INFO = None
            with open(file_name, "r") as sam_file:
                for line in sam_file:
                    if ">" in line:
                        if INFO != None：
                            data = (INFO, SEQ, START, END)
                            insert_data(c, table_name, data)

                        INFO = line
                        START = 
                        END = 
                    else:
                        line.replace("\n","")
                        line.replace("\r","")
                        SEQ = SEQ + line
                        
            data = (INFO, SEQ, START, END)
            insert_data(c, table_name, data)
                        
    
    conn.commit()
    conn.close()