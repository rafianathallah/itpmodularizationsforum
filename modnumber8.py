def find_longest_word(lwords):
    longestword = max(lwords, key=len)
    print("Longest word:",longestword)
    print("Length:",len(longestword))
    
find_longest_word(["Am","I","The","Longest"])