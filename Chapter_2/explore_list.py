vowels = ['a','e','i','o','u']
word = input("Provide a word to search for vowels:")
found =[]
for letters in word:
    if letters in vowels:
        if letters not in found:
            found.append(letters)
for vowels in found:
    print([vowels])
