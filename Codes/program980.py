class Arithematic:

    # Constructor
    def __init__(self, A = 0, B = 0):
        self.No1 = A        # Characteristics
        self.No2 = B        # Characteristics

    def Addition(self):
        Ans = 0
        Ans = self.No1 + self.No2
        return Ans
    
    def Substraction(self):
        Ans = 0
        Ans = self.No1 - self.No2
        return Ans

def main():

    Aobj = Arithematic()

    Ret = Aobj.Addition()
    print("Addition is : ", Ret)

    Ret = Aobj.Substraction()
    print("Substraction is : ", Ret)
   
main()