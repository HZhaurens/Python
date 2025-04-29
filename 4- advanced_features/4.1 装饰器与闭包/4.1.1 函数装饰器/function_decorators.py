"""
函数装饰器示例
====================

本模块演示Python函数装饰器的基本用法:

1. 基础装饰器
2. 带参数的装饰器
3. 保留函数元信息的装饰器
"""

# 基础装饰器
def simple_decorator(func):
    def wrapper():
        print("装饰器: 在函数调用前执行")
        func()
        print("装饰器: 在函数调用后执行")
    return wrapper

@simple_decorator
def say_hello():
    print("Hello!")

# 带参数的装饰器
def repeat(num_times):
    def decorator_repeat(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat

@repeat(num_times=3)
def greet(name):
    print(f"Hello {name}")

# 保留元信息的装饰器
from functools import wraps

def preserve_metadata(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """包装函数的文档字符串"""
        return func(*args, **kwargs)
    return wrapper

@preserve_metadata
def original_function():
    """原始函数的文档字符串"""
    pass