def buildtable(values,filename):
    writeString = ""
    filename = filename + ".dat"
    for i in range(len(values)):
        for j in range(len(values[i])):
            writeString = writeString + str(values[i][j]) + '\t'
        writeString = writeString + '\n'

    with open(filename,"w") as fp:
        fp.write(writeString)

    return