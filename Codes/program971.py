def CountCapital(Brr):

    iCount = 0

    for ch in Brr:
        if(ch >= 65 and ch <= 90):      # ISSUE
            iCount = iCount + 1


def main():
    print("Enter String : ")
    Arr = input()

    Ret = CountCapital(Arr)

    print("Number of capital characters are : ",Ret)
    
main()