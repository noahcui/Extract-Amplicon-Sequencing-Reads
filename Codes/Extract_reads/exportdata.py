#!/usr/bin/python

import sys
import sqlite3
import pickle
import time
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord

def buildreceivers(file_name):
    d = {}
    for n in file_name:
        reads = []
        d[n] = reads
    return d

def find(c, cv, q, dv):
    f1 = open(cv)
    f2 = open(q)
    f3 = open(dv)
    cmd1 = f1.read()
    cmd2 = f2.read()
    cmd3 = f3.read()
    cmd4 = "select distinct FILE from sam"
    if "forward" in q:
    	cmd5 = "select count(*) from sam where FLAG & 64 > 0 and FLAG < 2048"
    else:	
    	cmd5 = "select count(*) from sam where FLAG & 128 > 0 and FLAG < 2048"
    c.execute(cmd5)
    for row in c:
    	number = row[0]
    c.execute(cmd4)
    file_name = []
    for row in c:
        file_name.append(row[0])
    dic = buildreceivers(file_name)
    
    c.execute(cmd3)
    c.execute(cmd1)
    c.execute(cmd2)
    for row in c:
    	num = row[5]
    	p = 0.0
    	p = 1-(num / number)
    	nt = number/1.0 
    	n1 = num/1.0
    	print("extracted: ", num, "total: ",number, "lost: ", number - num, "lost percentage: ", (nt - n1)/nt * 100)
        chop = row[3]
        q = row[2][chop : len(row[2])]
        seq = row[0][chop : len(row[2])]
        seq = seq.replace('U', 'T')
        f_name = row[4]
        quality = {"phred_quality": [ord(char)-33 for char in q]} #row[2] is the  QUAL in SAM
        record = SeqRecord(seq, id=row[1], letter_annotations = quality) #row[0] is SEQ in SAM, and row[1] is REFNAME in SAM
        dic[f_name].append(record)
    return dic

if __name__ == '__main__':
    start = time.time()
    conn = None
    dbname = sys.argv[1]
    cv = sys.argv[2]
    q = sys.argv[3]
    dv = sys.argv[4]
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    dic = find(c, cv, q, dv)
    for n in dic:
        reads = dic[n]
        fastq = dbname.replace('.db', '') + "/" + n.replace('.sam','') + q.replace('.sql', '') + ".fastq"
        SeqIO.write(reads, fastq, "fastq")
    conn.commit()
    conn.close()
    end = time.time()
    print("time used: ", end - start)
