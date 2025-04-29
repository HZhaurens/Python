"""
类装饰器示例
====================

本模块演示Python类装饰器的基本用法:

1. 基础类装饰器
2. @classmethod和@staticmethod装饰器
"""

# 基础类装饰器
def class_decorator(cls):
    """添加新方法到被装饰的类"""
    def new_method(self):
        print("这是装饰器添加的新方法")
    
    cls.new_method = new_method
    return cls

@class_decorator
class MyClass:
    def original_method(self):
        print("这是原始方法")

# @classmethod和@staticmethod装饰器
class Calculator:
    @classmethod
    def class_method(cls):
        print(f"这是一个类方法，可以访问类属性 {cls.__name__}")
    
    @staticmethod
    def static_method():
        print("这是一个静态方法，不接收self或cls参数")