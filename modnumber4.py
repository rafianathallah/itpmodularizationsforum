def is_member(val, a):
    if a.count(val) >= 1:
        return True
        print("True")
    else:
        return False
        print("False")
            
print(is_member(2, [1,2,3]))
print(is_member(4, [1,2,3]))