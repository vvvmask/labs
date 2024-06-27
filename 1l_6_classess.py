class Person:

    age = 15

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


a = Person(name='Dias')
print(a.get_name())
