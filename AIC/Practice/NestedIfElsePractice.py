permission = input("Enter who you want to visit: ")
food_choice = input("what you want to eat: ")

# Single choice
if (permission == 'mamu'):
    print("\nI am going to mamu's house.")

    if (food_choice == 'biryani'):
        print("You will get biryani")
    elif (food_choice == 'tea'):
        print("You will tea")
    else:
        print("You will not eat anything")
else :
    print("\nI am going to " + permission + "'s home.")

    if (food_choice == 'water'):
        print("You will get water")
    else:
        print("This person will not offer you any food.")