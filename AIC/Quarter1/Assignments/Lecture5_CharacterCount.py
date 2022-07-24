print("********************* Character Count *********************")
sentence = input("Enter sentence: ")
single_character = input("Enter character to count: ")
count = 0

for char in sentence:
    if (single_character == char):
        count+=1

print("Total count of character", single_character, "=", count)
    