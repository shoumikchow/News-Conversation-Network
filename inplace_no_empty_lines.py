import fileinput

for line in fileinput.FileInput("lol.csv",inplace=1):
    if line.rstrip():
        with open("final.csv","a") as output:
        	output.write(line)
