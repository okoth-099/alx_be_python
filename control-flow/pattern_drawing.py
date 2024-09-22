#pattern app
pattern = int(input("Enter the size of pattern: "))

c = 1

while c <= pattern:
    for i in range(pattern):
       print("*", end="")
    print()
    c+=1
