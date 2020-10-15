def makeForms(verb):
    word=""
    if verb.endswith("y"):
        word = verb[0:len(verb)-1]+"ies"
    elif verb.endswith("o") or verb.endswith("ch") or verb.endswith("s") or verb.endswith("sh") or verb.endswith("x") or verb.endswith("z"):
        word = verb + "es"
    else:   
        word = verb + "s" 
    return word
 
print("3rd person form:",makeForms("try"))
print("3rd person form:",makeForms("brush"))
print("3rd person form:",makeForms("run"))
print("3rd person form:",makeForms("fix"))
