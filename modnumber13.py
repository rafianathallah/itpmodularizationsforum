def makeForming(verb):
    word = ""
    vowels = ["a", "e", "i", "o", "u"]
    if verb == "be":
       word = verb + "ing"
    elif verb[-2::] == "ee":
       word = verb + "ing"
    elif verb[-2::] == "ie":
       word = verb[:-2].split()
       word = word[0] + "y" + "ing"
    elif verb[-1] == "e":
       word = verb[:-1].split()
       word = word[0] + "ing"
    elif verb[-1] not in vowels:
        if verb[:-2] not in vowels:
            if verb[-2:-1] in vowels:
               word = verb + str(verb[-1]) + "ing"
    else:
       word = verb + "ing"
    return word

 
print("Present particle:",makeForming("lie"))
print("Present particle:",makeForming("see"))
print("Present particle:",makeForming("move"))
print("Present particle:",makeForming("hug"))
print("Present particle:",makeForming("map"))