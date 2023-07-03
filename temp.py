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

#繼承
class Sales(Employee):
    def __init__(self):
        self.__quota = 0
    @property
    def quota(self):
        return self.__quota
    @quota.setter
    def quota(self, value):
        self.__quota = value    
s= Sales()
s.id = 1
s.quota= 1000000    
print(s.id,s.quota)