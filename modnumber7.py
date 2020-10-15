def wordmap():
    words = input("Insert words seperated by a comma: ")
    print(words)
    list(words)
    wordlist = words.split(",")
    numberlist = []
    for word in range(len(wordlist)):
        characters = len(wordlist[word])
        numberlist.append(characters)
    return numberlist

print(wordmap())
    