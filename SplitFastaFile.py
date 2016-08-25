'''
Usage: 
python SplitFastaFile.py <inputFile.fa>
'''
import sys

def getOutFileName(s): # {{{

    s = s.replace("\\", "_")
    s = s.replace("/", "_")
    s = s.replace("*", "_")
    s = s.replace("..", "_")
    s = s.replace("?", "_")
    s = s.replace(":", "_")
    s = s.replace("[", "(")
    s = s.replace("]", ")")
    s = s.replace("P <=", "LE")
    s = s.replace("<=", "LE")
    s = s.replace("<", " LT")
    s = s.replace(">=", "GE")
    s = s.replace("|","_")
    s = s.replace("\s+","+")
    s+=".fasta"

    return s.strip()
#}}}


seq = ''

for lines in open(sys.argv[1],'r'):
	if (lines.startswith(">")):
		id = lines
		outFile = lines.strip().replace(">","")
		outFile = open(getOutFileName(outFile), 'w')
		outFile.write(str(lines))
	if not (lines.startswith(">")):
		outFile.write(str(lines))
		
