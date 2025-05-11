myList = [(1,2),(3,4),(5,6)]

def summ(x,y):
    return x+y

for k in myList:
    result = summ(*k)
    print(result)






