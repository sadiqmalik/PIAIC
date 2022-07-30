print("********************* Characters Count *********************")
sentence = input("Enter sentence: ")
characters_count = {}

for char in sentence.lower():
    if char in characters_count:
        characters_count[char] += 1
    else:
        characters_count[char] = 1

for key, value in characters_count.items():
    print(f'{key}: {value}')
