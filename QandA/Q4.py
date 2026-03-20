# Accept one number from user and print that number of * on screen

def Accept(No):

    for i in range(5):
        print("*",end=" ")
    
    print()

def main():
    
    print("Enter number : ")
    Value = int(input())

    Accept(Value)
    
main()