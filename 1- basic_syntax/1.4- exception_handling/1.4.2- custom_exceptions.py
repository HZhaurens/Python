# 自定义异常类示例

class InvalidAgeError(Exception):
    """年龄无效异常"""
    def __init__(self, age, message="年龄必须在0-120之间"):
        self.age = age
        self.message = message
        super().__init__(self.message)
    
    def __str__(self):
        return f"{self.age} -> {self.message}"

class NegativeValueError(Exception):
    """负值异常"""
    pass

def check_age(age):
    if age < 0:
        raise NegativeValueError("年龄不能为负数")
    elif age > 120:
        raise InvalidAgeError(age)
    print(f"年龄验证通过: {age}")

# 测试用例
print("\n=== 自定义异常类示例 ===")
try:
    check_age(25)  # 正常情况
    check_age(-5)  # 负值异常
    check_age(150) # 无效年龄异常
except NegativeValueError:
    print("捕获到负值异常")
except InvalidAgeError as e:
    print(f"捕获到无效年龄异常: {e}")