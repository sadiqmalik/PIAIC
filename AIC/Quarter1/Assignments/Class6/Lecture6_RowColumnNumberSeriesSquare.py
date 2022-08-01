print("************* Print Number Series Square *************\n")

while True:
    try:
        number = int(input("Please enter a number 1-9: "))

        if (number > 9):
            continue
        
        break
    except ValueError:
        print("Only number allowed!")

# Print number triangle
for i in range(number):
    current_number = number-i

    for j in range(current_number):
        print(" ", end="")

    if (i != 0):
        print (current_number, end="")

        for k in range(i+i-1):
            print(" ", end="")

    print(current_number)

# Print reverse number triangle
current_number += 1
for current_number in range(current_number, number+1):
    for j in range(current_number):
        print(" ", end="")
    
    print (current_number, end="")
    
    if (current_number == number):
        print("")
        break

    for s in range(number*2-current_number*2-1):
        print(" ", end="")

    print(current_number)
