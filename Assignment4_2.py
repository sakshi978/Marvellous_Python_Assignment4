def main():
    print("Enter numbers: ")
    iValue1 = int(input())
    iValue2 = int(input())

    fp = lambda no1,no2:no1*no2
    iRet = fp(iValue1,iValue2)
    print("Multiplication : ",iRet)

if __name__=="__main__":
    main()