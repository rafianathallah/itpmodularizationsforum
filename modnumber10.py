def pangramchecker(str):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for characters in alphabet:
        if characters not in str.lower():
            return False
        
    return True
    
        
sentence = str(input("Enter a sentence: "))
if(pangramchecker(sentence) == True):
    print("This sentence is a pangram.")
else:
    print("This sentence is not a pangram.")
