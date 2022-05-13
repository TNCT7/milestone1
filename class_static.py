class Foo:
    @classmethod
    def hi(cls):
        print(cls.__name__)


class Bar:
    @staticmethod
    def hi():
        print('Doesnt take any arguments')


s1= Foo()
s1.hi()

s2=Bar()
s2.hi()