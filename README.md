# Extract-Amplicon-Sequencing-Reads

* Database to extract amplicon sequencing reads from awhole metagenomic shotgun dataset and to format the extracted ampliconsequencing reads for traditional amplicon analysis in QIIME 2

* Use commercially available “universal” primer sequences to target 16S variableregions.

* Compare and contrast taxonomic assignments using 2 16S reference databases: GreenGenes and Silva (could add others)

* Compare and contrast analyses of extracted amplicon data to whole shotgunmetagenomic data (alignments, taxonomic assignments, community structure, andgene catalogues)

## 📌Use

* Allignment stats:

  * Counting total no. of alignments: `python count.py samfile` 
  * Counts of organism: `python Pal_Result.py tsvfile`
  * Counts of eukaryote: `python check_eukaryote.py samfile output.txt`
 
 * Datebase: 
 
   * - [Codes/Extract_reads/](https://github.com/hkcyf369/MCBS913-addiction/blob/master/Codes/Extract_reads/README.md)

## 📌Notice

* Extracting and sequencing could take a while. So, if you are running on a server and connecting thu ssh, it may be a good idea to run in background(&) or run a new tmux session:  ` tmux new -s mysession`

