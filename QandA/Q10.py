#  Accept one character from user and convert case of that character.

def DisplayConvert(Value):

    if(Value >= 'a' and Value <= 'z'):
        print(chr(ord(Value) - 32))
    elif(Value >= 'A' and Value <= 'Z'):
        print(chr(ord(Value) + 32))
    else:
        print(Value)

def main():
    
    print("Enter character : ")
    Value = input()

    DisplayConvert(Value)
    
main()