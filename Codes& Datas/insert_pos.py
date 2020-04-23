#!/usr/bin/python

import sys
import sqlite3

def create_table(c, table_name):
    cmd = "create table " + table_name + "(Header text,\
        start_POS int);"
    c.execute(cmd)
    print("table created successfully, now inserting datas")

def insert_forward(c, table_name, data):
    cmd = "INSERT OR IGNORE INTO " + table_name + " (Header, F_start_POS) VALUES(?,?);"
    cmd2 = "UPDATE " + table_name + " SET F_start_POS = ? WHERE Header = ?;"
    c.execute(cmd, data)
    data2 = (data[1],data[0])
    c.execute(cmd2, data2)

def insert_reverse(c, table_name, data):
    cmd = "INSERT OR IGNORE INTO " + table_name + " (Header, R_start_POS) VALUES(?,?);"
    cmd2 = "UPDATE " + table_name + " SET R_start_POS = ? WHERE Header = ?;"
    c.execute(cmd, data)
    data2 = (data[1],data[0])
    c.execute(cmd2, data2)


if __name__ == '__main__':
    conn = None
    dbname = sys.argv[1]
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    table_name = "startPOS"
    for i in range(len(sys.argv)):
        if i > 1:
            #directiory
            h = False
            file_name = sys.argv[i]
            if 'Forward' in file_name:
                F = True
            else: 
                F = False
            print("file: ", file_name)
            with open(file_name, "r") as pos_file:
                for line in pos_file:
                    fields = line.split(" ")
                    if h:
                        if 'Starting' in line:
                            POS = fields[2].replace('\n','')
                            h = False
                            data = (Header, POS)
                            if F :
                                insert_forward(c, table_name, data)
                            else:
                                insert_reverse(c, table_name, data)
                            
                        else:
                            POS = -1
                            h = False
                            data = (Header, POS)
                            if F :
                                insert_forward(c, table_name, data)
                            else:
                                insert_reverse(c, table_name, data)

                            if 'Header' in line:
                                h = True
                                Header = fields[1].replace('>','')
                    else:
                        if 'Header' in line:
                            h = True
                            Header = fields[1].replace('>','')
                    
    conn.commit()
    conn.close()