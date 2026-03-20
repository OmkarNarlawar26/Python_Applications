# Write a proge=ram which accept number from user and print even factors of that number

def DisplayEvenFactors(No):

    if(No <= 0):
        No = -No
    
    for i in range(1,int(No/2) + 1):

        if(((No % i) == 0) and ((i % 2) == 0)):
            print(i)

def main():
    
    print("Enter number : ")
    Value = int(input())

    DisplayEvenFactors(Value)
    
main()