

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
		