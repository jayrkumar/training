file = open("./data/test.txt", "r")
count = 0
for line in file:
	words = line.split(" ")
	count += len(words)
file.close()
print("Number of words in a Text File", count)
