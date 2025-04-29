# 类属性示例

class Car:
    """
    汽车类，展示类属性的使用
    """
    # 类属性
    wheels = 4
    
    def __init__(self, brand, model):
        # 实例属性
        self.brand = brand
        self.model = model
    
    def display_info(self):
        print(f"品牌: {self.brand}, 型号: {self.model}, 轮子数: {self.wheels}")

# 创建对象
car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")

# 访问类属性
print(f"所有汽车都有 {Car.wheels} 个轮子")

# 修改类属性会影响所有实例
Car.wheels = 3
print(f"现在所有汽车都有 {Car.wheels} 个轮子")

# 显示车辆信息
car1.display_info()
car2.display_info()