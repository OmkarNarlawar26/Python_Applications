# Write a program which accept number from user and display all its non factors.

def NonFact(No):

    Mult = 1

    for i in range(1, No):

        if(No % i != 0):
            print(i)
        
def main():
    
    print("Enter Number : ")
    Value = int(input())

    NonFact(Value)
    
main()