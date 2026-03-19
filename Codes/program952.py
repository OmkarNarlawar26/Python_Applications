def SumDigits(No):
    
    Digit = 0
    Sum = 0

    while(No != 0):
        Digit = No % 10
        Sum = Sum + Digit
        No = No // 10

    return Sum

def main():

    No = 0

    print("Enter number : ")
    No = int(input())

    Ret = SumDigits(No)

    print("Summation of Digits : ",Ret)
    
main()