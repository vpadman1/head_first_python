vowels = ['a','e','i','o','u']
word = input("Provide a word: ")

found = {}

for letter in word:
    if letter in vowels:
        found[letter] += 1

for k, v in sorted(found.items()):
    print(f"{k} was found {v} times")