print("************* Vowel & Consonant Count *************")
sentence = input("Enter sentence: ")

vowel = ("a", "e", "i", "o", "u")
characters_count = {"Vowels": 0, "Consonants": 0}

for char in sentence.lower():
    if char in vowel:
        characters_count['Vowels'] += 1
    else:
        characters_count['Consonants'] += 1

print(f'\nTotal Vowels: {characters_count["Vowels"]}', f'Total Consonants: {characters_count["Consonants"]}', sep="\n")
