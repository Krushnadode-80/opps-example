class Complex:
    def __init__(self,real,img):
        self.real =real
        self.img = img

    def show(self):
        print(self.real,"i",self.img,"j")

    def __add__(self,num2):
        sr =self.real +num2.real
        si =self.img +num2.img
        return Complex(sr, si)


    def __sub__(self,num2):
        sr =self.real -num2.real
        si =self.img -num2.img
        return Complex(sr, si)


num1 =Complex(1,2)
num1.show()

num2 =Complex(11,2)
num2.show()

num3 =num1 - num2
num3.show()
