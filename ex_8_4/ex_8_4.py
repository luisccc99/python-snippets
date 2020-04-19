fname = input("Enter file name: ")
fh = open(fname)
lst = list()
words = list()
for line in fh:
	line = line.rstrip()
	words = words + line.split()

for i in range(len(words)):
	if words[i] not in lst:
		lst.append(words[i])
lst.sort()
print(lst)


