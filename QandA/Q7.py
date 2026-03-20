# Accept two numbers from user and display first number in second number of times

def PrintEven(No):

    if(No <= 0):
        return 0
    
    for i in range(No*2):

        if(i % 2 == 0):
            print(i)

def main():
    
    print("Enter number : ")
    Value = int(input())

    PrintEven(Value)
    
main()