## 通过这个工资结算系统来说明面向对象中的三大支柱：继承、封装、多态

from abc import ABCMeta, abstractmethod

class Employee(metaclass=ABCMeta):
    """
    员工：抽象类，
    一个抽象的员工类，可以通过它来对各种员工的各种属性进行定义
    """
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_salary(self):
        """
        薪水计算：抽象方法，不用具体定义，通过类扩展成具体计算方法
        :return:
        """
        pass

class Manager(Employee):                       # 定义一种员工
    def get_salary(self):
        return 15000.0

class Programmer(Employee):
    def __init__(self, name, time):
        super(Programmer, self).__init__(name)
        self.time = time
    def get_salary(self):
        return 180.0*self.time

class Saleman(Employee):
    def __init__(self, name, sales):
        super(Saleman, self).__init__(name)
        self.sales = sales
    def get_salary(self):
        return 0.5*self.sales

class EmployeeFactory:
    """创建员工的工厂（通过工厂模式实现对象使用者和对象的解耦合）"""
    """通过这个类来对调用者和内部代码进行连接"""
    """
    在设计模式中主要用于抽象对象的创建过程，让用户可以指定自己想要的对象而不必关心对象的实例化过程。
    这样做的好处是用户只需通过固定的接口而不是直接去调用类的实例化方法来获得一个对象的实例，隐藏了实例创建过程的复杂度，
    解耦了生产实例和使用实例的代码，降低了维护的复杂性。详见参考文档。
    """
    @staticmethod                                      # 静态方法，使用该方法和类关系不大
    def create(emp_type, *args, **kwargs):
        """创建员工"""
        Employee_dict = {'M':Manager, 'P':Programmer, 'S':Saleman}
        cls = Employee_dict[emp_type.upper()]
        return cls(*args, **kwargs) if cls else None

def Main():
    emps = [
        EmployeeFactory.create('M', '111'),            # 为什么非得通过调用类中的方法来创建对象呢
        EmployeeFactory.create('P', '222', 168.5),
        EmployeeFactory.create('S', '333', 1999999)
    ]
    for emp in emps:
        print(f'{emp.name}:{emp.get_salary():.2f}元')

if __name__=='__main__':
    Main()