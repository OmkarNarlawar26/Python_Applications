# Program to Divide two numbers

def Divide(No1, No2):

    Ans = 0

    if(No2 == 0):
        return 0
    
    Ans = No1 / No2

    return Ans

def main():
    value1 = 15
    value2 = 5

    Ret = Divide(value1,value2)

    print("Division is : ",Ret)

main()