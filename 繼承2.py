class B1:
    def f1(self):
        print('B1::f1()')
class C1(B1):
    def f1(self):
        print('C1::f1()')
    def f2(self):
        #self.f1() #執行本身的程式
        super().f1() #執行副類別的子程式

c= C1()
c.f2()
