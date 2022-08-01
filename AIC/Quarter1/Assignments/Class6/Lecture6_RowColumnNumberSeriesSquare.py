print("************* Print Number Series Square *************\n")

while True:
    try:
        number = int(input("Please enter a number 1-9: "))

        if (number > 9):
            continue

        break
    except ValueError:
        print("Only number allowed!")

print("")

# Constant for show how wide the square should be!
# Change to 1,2,3,4... in order to see the gap 
SPACES_RATIO = 2
# Print number triangle
for i in range(number):
    current_number = number-i

    for j in range(current_number*SPACES_RATIO):
        print(" ", end="")

    if (i != 0):
        print (current_number, end="")

        for k in range(i*SPACES_RATIO*2-1):
            print(" ", end="")

    print(current_number)

# Print reverse number triangle
current_number += 1
for current_number in range(current_number, number+1):
    for j in range(current_number*SPACES_RATIO):
        print(" ", end="")
    
    if (current_number == number):
        print (current_number)
        break
    else:
        print (current_number, end="")

    inner_spaces_range = number*SPACES_RATIO*2-current_number*SPACES_RATIO*2-1

    for s in range(inner_spaces_range):
        print(" ", end="")

    print(current_number)
