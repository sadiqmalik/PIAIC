import random

random_list = []

def getRandomNumbers():
    global random_list

    while True:
        try:
            number = int(input("Please enter random number range: "))

            for i in range(number):
                random_list.insert(i, random.randint(1, 100))
            break;

        except ValueError:
            print("Only number allowed.")

# Greater than 40 list
def getGreaterThan40List():
    filtered_list = []

    for item in random_list:
        # Skip if value is less than equal to 40
        if (item<=40):
            continue

        filtered_list.append(item)

    return filtered_list

# Sum of random number list
def getRandomListSum():
    list_sum = 0

    for item in random_list:
        list_sum += item

    return list_sum

# Get Minimum value using loop
def getRandomListMinimumValue():
    minimum_value = 0

    for item in random_list:
        if (minimum_value == 0 or minimum_value > item):
            minimum_value = item

    return minimum_value

# Get Maximum value using loop
def getRandomListMaximumValue():
    minimum_value = 0

    for item in random_list:
        if (minimum_value == 0 or minimum_value < item):
            minimum_value = item

    return minimum_value

print("\n********************* Random Nummbers *********************\n")
getRandomNumbers()
print("Random list: ", random_list)
print("\nGreater than 40 list: ", getGreaterThan40List())
print("\nSum of random list: ", getRandomListSum())
print("Minimum of random list: ", getRandomListMinimumValue())
print("Minimum of random list with buil-in method: ", min(random_list))
print("\nMaximum of random list: ", getRandomListMaximumValue())
print("Maximum of random list with buil-in method: ", max(random_list))
