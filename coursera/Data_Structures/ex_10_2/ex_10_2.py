name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
words = list()
hours = dict()
for line in handle :
	line = line.split()
	if len(line) < 3 or line[0] != "From":
	 	continue
	line = line[-2].split(":")
	hours[line[0]] = hours.get(line[0], 0) + 1

reversedHours = sorted(hours.items())
for k, v in reversedHours :
	print(k, v)

# print(hours)
