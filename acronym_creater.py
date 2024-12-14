
word=input("Enter your words: ").strip()
words=word.split()
print(words)
acronym=''.join(w[0].upper() for w in words)
print(f"Acronym for '{word}' : {acronym}")