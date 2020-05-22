SELECT SEQ, REFNAME, QUAL, R_start_POS - POS + 20, FILE, count(*)
FROM BIO WHERE FLAG & 128 > 0 and R_start_POS + 20 <= POS + 100 and POS <= R_start_POS + 20 and flag < 2048;
