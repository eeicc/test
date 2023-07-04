from abc import ABC,abstractclassmethod
#Abstrsct Base Classes

#封裝:利用公開的方法存取私有屬性
class Employee(ABC):
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
    @abstractclassmethod #抽象
    def salary(self):
        pass

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
    def salary(self):
        return 20000 + self.__quota/10
        
s= Sales()
s.quota = 100000
print(s.salary())

