class Cat:
    def __init__(self, name):
        self._name = name
        self._say_name()

    def _say_name(self):
        print(f"Hello! My name is {self._name}!")

kitty = Cat('Sophie')