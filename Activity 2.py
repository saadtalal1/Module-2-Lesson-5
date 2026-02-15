rows=int(input("Enter the number of rows for your  pattern: "))
print("Floyd's pattern: ")
num=1
for i in range(rows):
    for j in range(i+1):
        print(num,end=" ")
        num=num+1
    print()