permission = input("Enter who you want to visit: ")

# Single choice
if (permission == 'mamu'):
    print("I have permission to go to mamu's house.")
else:
    print("I dont have permission to go there.")

permission = input("\nEnter who you want to visit multiple choice: ")

# Single choice
if (permission == 'mamu'):
    print("I have permission to go to mamu's house.")
elif (permission == 'chachu'):
    print("I have permission to go to chachu's house.")
elif (permission == 'friend'):
    print("I have permission to go to friend's house.")
elif (permission == 'sadiq'):
    print("I have permission to go to sadiq's house.")
else :
    print("I dont have permission to go there.")