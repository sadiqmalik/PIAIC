random_list = []

# Print table function
def printTable():
    while True:
        try:
            number = int(input("Enter number to print desired table: "))
            for index in range(10):
                print(number, "x", index+1, "=", (index+1)*number)

            # Take input from user if they want to print more tables    
            choice = str(input("\nDo you want to print more? y/n: "))
            if (choice == 'y'):
                continue;
        
            break;
        except ValueError:
            print("Only number allowed.")

print("********************* Print Table *********************")
printTable()
