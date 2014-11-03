'''
Usage: 
1. Change the file name in line 6.
2. Run as 'python SplitFastaFile.py'
'''
file = open("data.fa",'r')

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
    s+=".fasta"

    return s.strip()
#}}}


seq = ''

for lines in file:
	if (lines.startswith(">")):
		id = lines
		outFile = lines.strip().replace(">","")
		outFile = open(getOutFileName(outFile), 'w')
		outFile.write(str(lines))
	if not (lines.startswith(">")):
		outFile.write(str(lines))
		
