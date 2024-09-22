# pattern drawing app

user_input = int(input("Enter the size of pattern: "))

c = 1

while c <= user_input:
    for i in range(user_input):
       print("*", end="")
    print()
    c+=1
