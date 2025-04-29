# 继承示例

# 单继承
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(f"{self.name} 发出声音")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} 汪汪叫")

# 多继承
class Flyable:
    def fly(self):
        print("飞起来了")

class Swimable:
    def swim(self):
        print("游起来了")

class Duck(Animal, Flyable, Swimable):
    def speak(self):
        print(f"{self.name} 嘎嘎叫")

# 测试单继承
dog = Dog("旺财")
dog.speak()

# 测试多继承
duck = Duck("唐老鸭")
duck.speak()
duck.fly()
duck.swim()