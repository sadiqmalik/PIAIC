
# Print table with desired numbers
print("********************* Print Table *********************")

while True:
    try:
        number = int(input("Enter number to print desired table: "))
        for index in range(1,11):
            print(f"{number} x {index} = {index*number}")

        # Take input from user if they want to print more tables    
        choice = str(input("\nDo you want to print more? y/n: "))
        if (choice == 'y'):
            continue;
    
        break;
    except ValueError:
        print("Only number allowed.")
