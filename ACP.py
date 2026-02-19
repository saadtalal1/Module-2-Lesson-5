rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):
    stars = "*" * i
    # Each row needs 2 spaces less than the row above it
    spaces = " " * (2 * (rows - i))
    print(stars + spaces + stars)
