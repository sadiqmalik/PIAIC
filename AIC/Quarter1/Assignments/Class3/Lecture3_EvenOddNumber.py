# Even or Odd number
print("********************* Even/Odd number *********************")
while True:
    try:
        number = int(input("Please enter number: "))

        if (number % 2 == 0):
            print("Your number is an EVEN number!")
        else:
            print("Your number is an ODD number!")
 
        choice = str(input("\nDo you want to print more? y/n: "))
        if (choice == 'y'):
            continue;
    
        break;
    except ValueError:
        print("Only number allowed.")
