# Accept one number from user if number is less than 10 then print Hello otherwise print Demo

def Display(No):

    if(No < 10):
        print("Hello")
    else:
        print("Demo")

def main():
    
    print("Enter number : ")
    Value = int(input())

    Display(Value)
    
main()