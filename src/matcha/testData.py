# coding=utf-8
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def __repr__(self, *args, **kwargs):
        return self.__str__(self, *args, **kwargs)

    def __str__(self, *args, **kwargs):
        return '[{0}, {1}]'.format(self.name, self.age)


personList = (Person('Riven', 23), Person('Tom', 25))
personList[0].set_age(25)

print(personList)
print(personList[0])

print(type(personList))

oneDict = {'a': 1, 'b': 2, 'c': 3}
print(sorted(oneDict))
vd = oneDict.get('d', None)
va = oneDict.get('a', None)
print(vd)
print(va)
