def main():
    iValue = int(input("Enter number: "))

    fp = lambda no:no*no
    iRet = fp(iValue)
    print("Power of 2: ",iRet)

if __name__=="__main__":
    main()