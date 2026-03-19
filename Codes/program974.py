# HeLlo -> hElLO
# HELLO -> hello
# hello -> HELLO

def ToggleCase(Brr):
    Result = ""

    for ch in Brr:
        if(ch >= 'A' and ch <= 'Z'):
            Result = Result + chr(ord(ch) + 32)
        else:
            Result = Result + chr(ord(ch) - 32)     # ISSUE may occure
    
    return Result

def main():
    print("Enter String : ")
    Arr = input()

    Ret = ToggleCase(Arr)

    print("Updated string is : ",Ret)
    
main()