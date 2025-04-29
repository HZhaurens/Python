# 条件语句示例

# 基本if语句
age = 18
if age >= 18:
    print("您已成年")

# if-else语句
num = 7
if num % 2 == 0:
    print("偶数")
else:
    print("奇数")

# if-elif-else语句
score = 85
if score >= 90:
    print("优秀")
elif score >= 80:
    print("良好")
elif score >= 60:
    print("及格")
else:
    print("不及格")

# 嵌套if语句
x = 10
y = 5
if x > 0:
    if y > 0:
        print("x和y都是正数")
    else:
        print("x是正数但y不是")
else:
    print("x不是正数")