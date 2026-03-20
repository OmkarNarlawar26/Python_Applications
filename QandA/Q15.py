# Write a program which accept number from user and return summation of all its non factors.

def SumNonFact(No):

    Sum = 0

    for i in range(1, No):

        if(No % i != 0):
            
            Sum = Sum + i

    return Sum
        
def main():
    
    print("Enter Number : ")
    Value = int(input())

    Ret = SumNonFact(Value)

    print("Summation of non factor is : ",Ret)
    
main()