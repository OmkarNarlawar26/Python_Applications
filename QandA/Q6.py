# Accept two numbers from user and display first number in second number of times

def Display(No, Frequency):

    if(Frequency < 0):
        Frequency = -Frequency
    
    for i in range(Frequency):
        print(No)

def main():
    
    print("Enter first number : ")
    Value1 = int(input())

    print("Enter second number : ")
    Value2 = int(input())

    Display(Value1, Value2)
    
main()