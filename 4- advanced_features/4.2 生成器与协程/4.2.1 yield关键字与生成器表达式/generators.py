"""
生成器示例
====================

本模块演示生成器的基本用法:

1. yield关键字的使用
2. 生成器表达式的应用
"""

# 简单生成器函数
def count_down(num):
    """倒计时生成器"""
    while num > 0:
        yield num
        num -= 1

# 生成器表达式
def generator_expression():
    """生成器表达式示例"""
    squares = (x*x for x in range(10))
    return squares

if __name__ == "__main__":
    print("生成器函数示例:")
    for i in count_down(5):
        print(i)
    
    print("\n生成器表达式示例:")
    squares = generator_expression()
    for num in squares:
        print(num)