#封裝:利用公開的方法存取私有屬性
class Employee:
    def __init__(self):
        self.__id = 0
        self.__name = ''
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self,value):
        if value < 0:    
            raise ValueError('ID輸入錯誤')
        self.__id=value
emp=Employee()
id=int(input('請輸入Id:'))
emp.id=id
name=input('請輸入Name:')
emp.name=name
print(emp.id,emp.name)
