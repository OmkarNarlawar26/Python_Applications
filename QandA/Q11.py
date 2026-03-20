# Accept on character from user and check whether that character is vowel (a,e,i,o,u) or not.


def ChkVowel(Value):

    if(Value == 'A' or Value == 'E' or Value == 'I' or Value == 'O' or Value == 'U' or Value == 'a' or Value == 'e' or Value == 'i' or Value == 'o' or Value == 'u'):
        return True
    else:
        return False

def main():
    
    print("Enter character : ")
    Value = input()

    Ret = ChkVowel(Value)

    if(Ret == True):
        print("It is Vowel")
    else:
        print("It is not Vowel")
    
main()