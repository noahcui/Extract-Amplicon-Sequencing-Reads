PUT ALL THOSE FILES UNDER THE SAME DIR WITH DB FILES
# Usage for this progect: 
  `./bash.run`
# Usage for exportdata.py: 
  `python exportdata.py DBNAME.db cv.sql SORTING_SQL_FILE.sql dv.sql`
--------------------------------------------------------------------------------
# Dealing with raw sam files(Doing quality filter in the Database):
  add: `FLAG & 4 = 0 and MAPQ > THE_MAPQ_YOU_NEED` and `to SORTING_SQL_FILE.sql`, after `where`
--------------------------------------------------------------------------------
SORTING_SQL_FILE.sql in this project is reverse.sql and forward.sql
