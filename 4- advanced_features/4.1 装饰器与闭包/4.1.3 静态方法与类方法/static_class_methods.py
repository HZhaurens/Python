"""
静态方法与类方法示例
====================

本模块演示Python中静态方法与类方法的基本用法:

1. @staticmethod装饰器
2. @classmethod装饰器
"""

class MyClass:
    class_attribute = "类属性"
    
    def __init__(self, value):
        self.instance_attribute = value
    
    @classmethod
    def class_method(cls):
        print(f"类方法可以访问类属性: {cls.class_attribute}")
        print("但不能直接访问实例属性")
    
    @staticmethod
    def static_method():
        print("静态方法既不能访问类属性也不能访问实例属性")
    
    def instance_method(self):
        print(f"实例方法可以访问实例属性: {self.instance_attribute}")
        print(f"也可以访问类属性: {self.__class__.class_attribute}")