# 方法重写示例

class Vehicle:
    def __init__(self, name):
        self.name = name
    
    def move(self):
        print(f"{self.name} 正在移动")

class Car(Vehicle):
    def move(self):
        print(f"{self.name} 在路上行驶")

class Boat(Vehicle):
    def move(self):
        print(f"{self.name} 在水上航行")

class Airplane(Vehicle):
    def move(self):
        print(f"{self.name} 在空中飞行")

# 创建对象
vehicle = Vehicle("交通工具")
car = Car("汽车")
boat = Boat("船")
airplane = Airplane("飞机")

# 调用重写的方法
vehicle.move()
car.move()
boat.move()
airplane.move()