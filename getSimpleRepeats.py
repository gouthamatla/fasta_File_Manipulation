'''
This script extract the coordinates of simple Repeat of 4. along with one extra base on either side. This is important because fo a SNP
is found in between two repeats but not with in the repeat, those shoud also be accounted. AAAAGAAAAA
And if a SNP is present at the end or begening of simple repeat GAAAAAA ot AAAAAG, those should be accounted.

Requirements: BioPython, bedtools

usage:
python getSimpleRepeats.py in.fasta | bedtools merge > out.bed

or to make it faster, run on individual chromosomes

parallel "python getSimpleRepeats.py {} | bedtools merge > {/.}.bed " ::: *.fa

'''

import re
import sys
from Bio import SeqIO

def return_simpleRepeats(id,seqence):
  pattern=r"A{4,}|G{4,}|C{4,}|T{4,}"
  repeat = ["\t".join((id, str(m.start()),str(m.end()+1))) for m in re.finditer(pattern,seqence)]
  if repeat:
		for i in repeat:
			print i	
for seq in SeqIO.parse(sys.argv[1],"fasta"):
	return_simpleRepeats(str(seq.id),str(seq.seq))
