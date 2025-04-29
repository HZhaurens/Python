"""
闭包示例
====================

本模块演示Python中闭包的基本用法:

1. 基础闭包
2. nonlocal关键字使用
"""

# 基础闭包
def outer_func(x):
    def inner_func(y):
        return x + y
    return inner_func

closure = outer_func(10)
print(closure(5))  # 输出15

# nonlocal关键字使用
def counter():
    count = 0
    
    def increment():
        nonlocal count
        count += 1
        return count
    
    return increment

my_counter = counter()
print(my_counter())  # 输出1
print(my_counter())  # 输出2