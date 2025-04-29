# 类定义与对象创建示例

class Person:
    """
    人类基本类
    """
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        print(f"大家好，我叫{self.name}，今年{self.age}岁。")

# 创建对象
person1 = Person("张三", 25)
person2 = Person("李四", 30)

# 调用方法
person1.introduce()
person2.introduce()