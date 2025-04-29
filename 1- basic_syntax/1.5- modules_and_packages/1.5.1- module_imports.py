# 模块导入与标准库使用示例

# 1. 基本导入方式
import math  # 导入整个模块
from random import randint  # 从模块导入特定函数
import datetime as dt  # 导入模块并设置别名
from time import *  # 导入模块中的所有内容
# 2. 标准库模块使用示例
def math_operations():
    """数学运算示例"""
    print("\n=== 数学运算示例 ===")
    print(f"圆周率: {math.pi}")
    print(f"2的平方根: {math.sqrt(2)}")
    print(f"5的阶乘: {math.factorial(5)}")

def random_examples():
    """随机数示例"""
    print("\n=== 随机数示例 ===")
    print(f"1到10的随机整数: {randint(1, 10)}")
    print(f"随机选择: {['苹果', '香蕉', '橙子'][randint(0, 2)]}")

def datetime_demo():
    """日期时间示例"""
    print("\n=== 日期时间示例 ===")
    today = dt.date.today()
    print(f"今天是: {today}")
    print(f"今天是星期: {today.strftime('%A')}")
    print(f"当前时间: {dt.datetime.now().time()}")
def time_demo():
    """时间示例"""
    print("\n=== 时间示例 ===")
    print(f"当前时间戳: {time()}")
# 3. 主程序
if __name__ == "__main__":
    math_operations()
    random_examples()
    datetime_demo()
    time_demo()
    print("\n所有示例执行完毕！")
