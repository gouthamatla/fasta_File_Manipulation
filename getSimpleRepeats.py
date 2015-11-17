'''
Requirements: BioPython

usage:
python getSimpleRepeats.py in.fasta | bedtools merge > out.bed

'''

import re
import sys
from Bio import SeqIO

def return_simpleRepeats(id,seqence):
  pattern=r"A{4,}|G{4,}|C{4,}|T{4,}"
  repeat = ["\t".join((id, str(m.start()+1),str(m.end()+1))) for m in re.finditer(pattern,seqence)]
  if repeat:
		for i in repeat:
			print i	
for seq in SeqIO.parse(sys.argv[1],"fasta"):
	return_simpleRepeats(str(seq.id),str(seq.seq))
