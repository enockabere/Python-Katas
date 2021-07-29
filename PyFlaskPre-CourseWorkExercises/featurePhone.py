print("Enter a string")

input_string = input()

characters = {}

for character in input_string:
    characters.setdefault(character,0)
    characters[character] = characters[character] + 1


print(character)
