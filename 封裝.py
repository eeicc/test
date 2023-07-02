#封裝:利用公開的方法存取私有屬性
class Employee:
    def __init__(self):
        self.__id = 0
        self.__name = ''
    #則一顯示 8~14 or 16~23
    
    # def set_id(self,value):
    #     if value <0:
    #         raise ValueError('ID輸入錯誤')
    #     self.__id=value
    # def get_id(self):
    #     return self.__id
    # id=property(fget=get_id,fset=set_id)
    
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self,value):
        if value < 0:    
            raise ValueError('ID輸入錯誤')
        self.__id=value
emp=Employee()
emp.id=1
print(emp.id)
