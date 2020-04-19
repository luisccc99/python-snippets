# sample = "X-DSPAM-Confidence: 0.8509"
# atpos = 0
# atpos = sample.find(" ")
# atpos = float(sample[atpos + 1:])
# print(type(atpos))
# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
avg = 0
count = 0
atpos = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    atpos = line.find(" ")
    avg = avg + float(line[atpos+1:])
    count = count + 1
    
print("Average spam confidence:", avg/count)
