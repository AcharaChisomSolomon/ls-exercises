class Cat:
    count = 0

    @classmethod
    def total(cls):
        print(Cat.count)
    
    def __init__(self):
        Cat.count += 1

Cat.total()         # 0

kitty1 = Cat()
Cat.total()         # 1

kitty2 = Cat()
Cat.total()         # 2

print(Cat())        # <__main__.Cat object at 0x104ed7290>
Cat.total()         # 3