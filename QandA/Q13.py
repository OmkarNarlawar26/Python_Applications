# Write a program which accept number from user and display its factors in decreasing order.

def FactRev(No):

    Mult = 1

    for i in range(int(No/2) + 1, 0, -1):

        if(No % i == 0):
            print(i)
        
def main():
    
    print("Enter Number : ")
    Value = int(input())

    FactRev(Value)
    
main()