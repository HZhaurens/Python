# 多态示例

class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "汪汪"

class Cat(Animal):
    def speak(self):
        return "喵喵"

class Duck(Animal):
    def speak(self):
        return "嘎嘎"

def animal_speak(animal):
    print(animal.speak())

# 创建不同动物对象
dog = Dog()
cat = Cat()
duck = Duck()

# 调用相同方法，不同表现
animal_speak(dog)
animal_speak(cat)
animal_speak(duck)