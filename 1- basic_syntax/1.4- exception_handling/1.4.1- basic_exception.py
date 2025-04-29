# 基本异常处理示例

def divide_numbers(a, b):
    try:
        result = a / b
        print(f"{a} 除以 {b} 的结果是: {result}")
    except ZeroDivisionError:
        print("错误：除数不能为零！")
    except TypeError:
        print("错误：请输入数字类型！")
    except Exception as e:
        print(f"发生未知错误: {e}")
    else:
        print("计算成功完成")
    finally:
        print("计算过程结束\n")

# 测试用例
print("=== 基本异常处理示例 ===")
divide_numbers(10, 2)  # 正常情况
divide_numbers(10, 0)  # 除零错误
divide_numbers("10", 2)  # 类型错误