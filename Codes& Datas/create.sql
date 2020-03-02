-- SQLite
create table Bacillus_anthracis_paired(
QNAME text PRIMARY KEY,
FLAG int,
RENAME text,
POS int,
MAPQ int,
CIGAR text,
RNEXT text,
PNEXT int,
TLEN int
);

create table Combined(
QNAME text PRIMARY KEY,
FLAG int,
RENAME text,
POS int,
MAPQ int,
CIGAR text,
RNEXT text,
PNEXT int,
TLEN int
);

create table Enterococcus_faecalis_paired(
QNAME text PRIMARY KEY,
FLAG int,
RENAME text,
POS int,
MAPQ int,
CIGAR text,
RNEXT text,
PNEXT int,
TLEN int
);

create table Staphylococcus_aureus_paired(
QNAME text PRIMARY KEY,
FLAG int,
RENAME text,
POS int,
MAPQ int,
CIGAR text,
RNEXT text,
PNEXT int,
TLEN int
);

create table Streptococcus_agalactiae_paired(
QNAME text PRIMARY KEY,
FLAG int,
RENAME text,
POS int,
MAPQ int,
CIGAR text,
RNEXT text,
PNEXT int,
TLEN int
);