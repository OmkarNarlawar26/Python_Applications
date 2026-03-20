# 5.Write a program which accept number from user and return difference between summation of all its factors and non factors.

def FactDiff(No):

    FactSum = 0
    NonFactSum = 0

    if(No <= 0):
        No = -No

    for i in range(1, No):

        if(No % i == 0):
            
            FactSum = FactSum + i
        else:
            NonFactSum = NonFactSum + i

    return (FactSum - NonFactSum)
        
def main():
    
    print("Enter Number : ")
    Value = int(input())

    Ret = FactDiff(Value)

    print("Difference of factor and  non factor is : ",Ret)
    
main()