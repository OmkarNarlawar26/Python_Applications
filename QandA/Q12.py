# Write a program which accept number from user and display its multiplication of factors.

def MultFact(No):

    Mult = 1

    for i in range(1, int(No/2) + 1):

        if(No % i == 0):
            Mult = Mult * i
        
    return Mult
    

def main():
    
    print("Enter Number : ")
    Value = int(input())

    Ret = MultFact(Value)

    print("Multiplication of factor is : ",Ret)
    
main()