print("************* Print Number Series *************")

while True:
    try:
        number = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Only number allowed!")

# Print empty line
print("")

for i in range(1, number+1):
    for i in range(1, number+1):
        print(i, end=" ")
    
    print("")
    number -= 1
