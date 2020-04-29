from Bio import SeqIO
from Bio.SeqRecord import SeqRecord

reads=[]
for seq in your_sequences:
    quality = dict("fastq": seq["quality"])
    record = SeqRecord(seq["sequences"], id=seq["id"], letter_annotations=quality)
    reads.append(record)
SeqIO.write(reads, "new_reads.fastq", "fastq")