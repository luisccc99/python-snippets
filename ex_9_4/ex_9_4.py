name = input("Enter file name: ")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

emails = dict()

for line in handle:
	line = line.split()
	if len(line) < 3 or line[0] != "From":
	 	continue
	emails[line[1]] = emails.get(line[1], 0) + 1

sender = None
count = None
for k, v in emails.items():
	if count is None or v > count:
		count = v
		sender = k
print(sender, count)
# print("There were", count, "lines in the file with From as the first word")