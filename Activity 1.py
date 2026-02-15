print("Half pyramid pattern of stars (*): ")
rows=int(input("Enter the number of rows for your  pattern: "))

for i in range(rows):
    for j in range(i+1):
        print("*",end="")
    print()