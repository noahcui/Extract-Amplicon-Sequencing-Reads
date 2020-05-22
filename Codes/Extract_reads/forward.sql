SELECT SEQ, REFNAME, QUAL, F_start_POS - POS + 20, FILE, count(*)
FROM BIO WHERE FLAG & 64 > 0 and F_start_POS + 20 <= POS + 100 and POS <= F_start_POS + 20 and flag < 2048;