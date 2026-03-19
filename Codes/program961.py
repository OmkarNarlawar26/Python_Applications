def Summation(Brr):

    Sum = 0

    # for i in range(len(Brr)):
    #     Sum = Sum + Brr[i]

    for no in Brr:
        Sum = Sum + no

    return Sum

def main():
    Size = 0
    Arr = []

    print("Enter number of elements : ")
    Size = int(input())

    print("Enter the elements : ")

    Value = 0

    for i in range(Size):
        Value = int(input())
        Arr.append(Value)

    print(Arr)

    Ret = Summation(Arr)

    print("Summation is : ",Ret)
    
main()