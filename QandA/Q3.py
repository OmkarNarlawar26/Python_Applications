# Accept one number and check whether it is divisible by 5 or not.

def Check(No):

    return (No % 5 == 0)

def main():
    
    print("Enter number : ")
    Value = int(input())

    Ret = Check(Value)

    if(Ret == True):
        print("Divisible by 5")    
    else:
        print("Not Divisible by 5")

    
main()