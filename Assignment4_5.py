import functools

arr = list()

num = int(input("Enter number of elements: "))

for i in range(0, num):
    no = int(input("Enter numbers: "))
    arr.append(no)

def ChkPrime(no):
    if no > 1:
        for i in range(2, no):
            if (no%i) == 0:
                return False
                break
        else:
            return True
    else:
        return False

def Mul2(no):
    return no*2

def Modify(no, iMax):
    if (no > iMax):
        iMax = no
    return iMax

ChkPrimearr = list(filter(ChkPrime,arr))
print("Data after filter: ", ChkPrimearr)

Mul2arr = list(map(Mul2, ChkPrimearr))
print("Data after map: ", Mul2arr)

modarr = functools.reduce(Modify, Mul2arr)
print("Maximum: ", modarr)