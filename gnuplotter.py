def buildtable(values):
	writeString = ""
	for i in range(len(values)):
		for j in range(len(values[i])):
			writeString = writeString + str(values[i][j]) + '\t'
		writeString = writeString + '\n'

	with open("data.txt","w") as fp:
		fp.write(writeString)

	return

def buildgraph(searchtype,yticks):
	with open("timings.gplot","r") as infile:
		outstring = infile.read();

	outstring = outstring + "    set output \"{0}.eps\"\n".format(searchtype)
	outstring = outstring + "    set yrange [0:{0}]\n".format(yticks)
	outstring = outstring + "    plot \\\n"
	outstring = outstring + "        \"{0}.out\" using 1:2 title \"{1}\"\n".format(searchtype,searchtype)

	with open("{0}.gplot".format(searchtype),"w") as outfile:
		outfile.write(outstring)

	return