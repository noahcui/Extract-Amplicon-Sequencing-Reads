#!/usr/bin/python

import sys
import sqlite3


def find(c):
    cmd = "select * from sam"
    c.execute(cmd)

if __name__ == '__main__':
    conn = None
    dbname = sys.argv[1]
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    rec = []
    find(c)
