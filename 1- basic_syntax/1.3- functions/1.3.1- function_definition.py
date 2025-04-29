# 函数定义与参数传递

# 基本函数定义
def greet(name):
    """简单的问候函数"""
    return f"Hello, {name}!"

# 默认参数
def power(base, exponent=2):
    """计算幂次，默认平方"""
    return base ** exponent

# 可变位置参数
def sum_all(*numbers):
    """计算任意数量数字的和"""
    total = 0
    for num in numbers:
        total += num
    return total

# 可变关键字参数
def print_info(**info):
    """打印任意键值对信息"""
    for key, value in info.items():
        print(f"{key}: {value}")

# 参数传递示例
print(greet("Alice"))
print(power(3))  # 使用默认参数
print(power(2, 3))  # 覆盖默认参数
print(sum_all(1, 2, 3, 4, 5))
print_info(name="Bob", age=30, city="New York")