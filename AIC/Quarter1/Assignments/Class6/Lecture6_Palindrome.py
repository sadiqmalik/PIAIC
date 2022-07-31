print("************* Print Number Series *************")

string = input("Please enter string: ")
string_length = len(string)
is_palindrome = True

for i in range(string_length):
    # Check if the index is middle of string
    if i == int(string_length/2):
        break;
        
    if string[i] != string[-1-i]:
        is_palindrome = False
        break

if (is_palindrome and string_length > 0):
    print("\nString is palindrome!")
else:
    print("\nString is not palindrome!")