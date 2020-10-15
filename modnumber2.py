def translate(text):
    
    word = ""
#consonants: everything but aiueo i think?

    for letter in range(len(text)):
       if text[letter] == "a":
           word += text[letter]
       elif text[letter] == "i":
            word += text[letter]
       elif text[letter] == "u":
            word += text[letter]
       elif text[letter] == "e":
            word += text[letter]
       elif text[letter] == "o":
            word += text[letter]  
       else:
            word = word + text[letter] + "o" + text[letter]
    return word

sentence = (input("Sentence to be translated: "))
print(sentence)
print(translate(sentence))
