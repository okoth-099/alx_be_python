#pattern app
length = int(input("Enter the size of pattern: "))

c = 1

while c <= length:
    for i in range(length):
       print("*", end="")
    print()
    c+=1
