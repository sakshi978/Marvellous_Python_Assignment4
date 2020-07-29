import functools

arr = list()

num = int(input("Enter number of elements: "))

for i in range(0, num):
    no = int(input("Enter numbers: "))
    arr.append(no)

def SevenToNine(no):
    for i in range(0, num):
        if (no >= 70 and no <= 90):
            return no

def Increase(no):
    return no+10

def Modify(no, iMult):
    return iMult*no

seventonine = list(filter(SevenToNine,arr))
print("Data after filter: ", seventonine)

incr = list(map(Increase, seventonine))
print("Data after map: ", incr)

modarr = functools.reduce(Modify, incr)
print("Mult: ", modarr)