# 实例方法示例

class Calculator:
    """
    计算器类，展示实例方法的使用
    """
    def __init__(self):
        self.result = 0
    
    def add(self, num):
        """加法方法"""
        self.result += num
        return self
    
    def subtract(self, num):
        """减法方法"""
        self.result -= num
        return self
    
    def multiply(self, num):
        """乘法方法"""
        self.result *= num
        return self
    
    def divide(self, num):
        """除法方法"""
        self.result /= num
        return self

# 使用方法链式调用
calc = Calculator()
calc.add(10).subtract(5).multiply(3).divide(2)
print(f"计算结果: {calc.result}")