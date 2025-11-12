



class Account:
    def __init__(self,acc_no,acc_pass):  #Attribute
        self.acc_no =acc_no
        self.__acc_pass =acc_pass

    def reset_(self):      #Methods
        print(self.__acc_pass)

a1 =Account("12021","123@")
a2 =Account("12022","123@")


print(a1.acc_no)
print(a1.reset_())

print(a2.acc_no)
print(a2.reset_())