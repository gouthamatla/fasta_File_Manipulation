import sys

def getChrSize(fileName):
    seq = ""
    ids = []
    seqLen = []
    for line in fileName:
        if (line.startswith(">")):
            id = line.strip()
            if ( len(seq) > 0 ):
                seqLen.append(len(seq))
                seq = ""
            ids.append(id[1:])    
        else:
            seq = seq + line.rstrip()
    seqLen.append(len(seq.strip()))
    
    return zip(ids, seqLen)


Args = str(sys.argv)

FileArgument = open(sys.argv[1],'r')
#OutFile = open('Args[1]','w')

ChrSizeMap = getChrSize(FileArgument)

for id,seq in ChrSizeMap:
	print id+"\t"+str(seq)
