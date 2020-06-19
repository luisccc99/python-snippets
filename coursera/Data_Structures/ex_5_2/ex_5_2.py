largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" : break
        
    try:
        num = int(num)
    except:
        print("Invalid input")
        continue
        
    if largest is None or smallest is None:
        largest = num
        smallest = num
    else:
        if largest < num:
            largest = num
        elif smallest > num:
            smallest = num   
    
    print(num)

print("Maximum is", largest)
print("Minimum is", smallest)