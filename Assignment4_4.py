import functools

arr = list()

num = int(input("Enter number of elements: "))

for i in range(0, num):
    no = int(input("Enter numbers: "))
    arr.append(no)

def Evenchk(no):
    return (no%2==0)

def Square(no):
    return no*no

def Modify(no, iSum):
    return iSum+no

evenchkarr = list(filter(Evenchk,arr))
print("Data after filter: ", evenchkarr)

squarearr = list(map(Square, evenchkarr))
print("Data after map: ", squarearr)

modarr = functools.reduce(Modify, squarearr)
print("Addition: ", modarr)