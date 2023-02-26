animal = "Canis lupus"
array = animal.split()
word = f"{array[0]} {array[1].capitalize()} {4 + 5}"

print(word)
print(array[0])
print(animal.upper())
print(animal.lower())
print(animal.strip().capitalize())
print(animal.title())
print(animal.lstrip())
print(animal.rstrip())
print(animal.find("u"))
print(animal.replace("u", "e"))
print("an" in animal)
print("lu" not in animal)
