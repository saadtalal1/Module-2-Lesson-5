rows=int(input("Enter the number of rows for your  pattern: "))
print("Diamond pattern")
num=1
space=" "
for i in range(rows):
    for j in range(rows-i):
        print(" ",end="")
    for k in range(i):
        print("* ",end="")
    print()

for i in range(rows-1,0,-1):
    for j in range(rows-i):
        print(" ",end="")
    for k in range(i):
        print("* ",end="")
    print()