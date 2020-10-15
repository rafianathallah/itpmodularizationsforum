def filter_long_words(lwords):
    n = int(input("Insert integer: "))
    print(n)
    filteredlwords = [i for i in lwords if len(i) > n]
    print("Filtered words:",filteredlwords)
    
filter_long_words(["Which","One","Is","Longer","Than","The","Integer"])