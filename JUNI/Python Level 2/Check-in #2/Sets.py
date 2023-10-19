recipe = set()

recipe.add("chicken")
recipe.add("salt")
recipe.add("lemon")

recipe.remove("chicken")

print(recipe)

recipe2 = set()

recipe2.add("chicken")
recipe2.add("lemon")
recipe2.add("salt")

ingredients = set()

ingredients = recipe.union(recipe2)

print(ingredients)

ingredients = recipe.intersection(recipe2)

print(ingredients)

recipe.add("garlic")
recipe2.add("garlic")


if "garlic" in recipe and "garlic" in recipe2:
  print("garlic is in both of your sets")
elif "garlic" in recipe or "garlic" in recipe2:
  print("Garlic is in one of your sets")
else:
  print("garlic is not in any of your sets")

banana = "banana"

letters = set()

for i in banana:
  letters.add(i)

print(letters)