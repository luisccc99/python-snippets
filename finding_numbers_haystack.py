import re
hand = open("regex_sum_678844.txt")
lst = list()
sum = 0
for line in hand:
    line = line.strip()
    numbers = re.findall('[0-9]+', line)
    if len(numbers) > 0:
        for num in numbers:
            num = int(num)
            lst.append(num)
            sum = sum + num
print('There are %d values and with a sum=%d' %(len(lst), sum))