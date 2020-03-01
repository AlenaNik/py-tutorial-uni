message = input("> ")
words = message.split(' ')
smiles = {
    ":)": "🙂",
    ":(": "😟",
    "house": "🏡"
}
output = ""
for word in words:
   output += smiles.get(word, word) + " "
print(output)