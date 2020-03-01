num = input("Phone: ")
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Tree"
}

output = ""
for ch in num:
   output += digits_mapping.get(ch, "Doesnt exist") + " "
print(output)