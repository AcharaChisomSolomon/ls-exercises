class Cat:
    COLOR = 'purple'

    def __init__(self, name):
        self._name = name

    def greet(self):
        print(f"Hello! My name is {self._name} and I'm a {Cat.COLOR} cat!")

cat = Cat('Sophie')
cat.greet()