def commonCharacterCount(a, b):
    a.sort()
    b.sort()
    result = [y - x for x,y in zip(a,b)]
    if sum(result)==0:
        return print("a")
    else:
        return print("b")
commonCharacterCount(a = [4,6,3] , b = [3,4,6])