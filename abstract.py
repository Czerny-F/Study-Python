from abc import ABC
# from abc import ABCMeta
from abc import abstractmethod


# class AbstractBaseClass(metaclass=ABCMeta):
class AbstractBaseClass(ABC):
    class_var = 'Abstract CLASS VARIABLE'

    def __init__(self):
        self.instance_var = 'INSTANCE VARIABLE'

    @classmethod
    def class_method(cls):
        print(cls, "by class method")
        print(cls.class_var, "by class method")

    @staticmethod
    def static_method():
        print(AbstractBaseClass, "by static method")
        print(AbstractBaseClass.class_var, "by static method")

    @abstractmethod
    def my_method(self):
        pass

    @abstractmethod
    def some_method(self):
        raise NotImplementedError()


class ConcreteClass(AbstractBaseClass):
    class_var = 'Concrete CLASS VARIABLE'

    @staticmethod
    def static_method():
        print(ConcreteClass, "by static method")
        print(ConcreteClass.class_var, "by static method")
        print(AbstractBaseClass.class_var, "by static method")

    def my_method(self, foo: str = 'foo'):
        print('concrete with %s' % foo)

    def some_method(self):
        print("some method implemented")


if __name__ == '__main__':
    abc = ConcreteClass()
    abc.my_method()
    abc.my_method(foo=1)
    abc.my_method('FOO')

    ConcreteClass.class_method()
    abc.class_method()

    abc.some_method()

    ConcreteClass.static_method()
    abc.static_method()

    print(ConcreteClass.class_var)
    print(AbstractBaseClass.class_var)

    print(abc.class_var)
    print(abc.instance_var)
