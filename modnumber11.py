def char_freq(string):
    wordfrequency = {}
    
    for character in string:
        if character in wordfrequency:
            wordfrequency[character] += 1
        else:
            wordfrequency[character] = 1
    print("Character frequencies in '{}' :\n {}".format(string, str(wordfrequency)))

char_freq("testing")