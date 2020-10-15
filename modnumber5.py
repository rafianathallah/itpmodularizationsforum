def overlapping(lst1, lst2):
    for i in lst1:
        for j in lst2:
            if lst1.count(j) >= 1:
                return True
                print("True")
            elif lst2.count(i) >= 1:
                return True
                print ("True")
            else:
                return False
                print ("False")

print(overlapping([1,2,3], [4,5,6]))
print(overlapping([1,2,3], [3,4,5]))

            
    