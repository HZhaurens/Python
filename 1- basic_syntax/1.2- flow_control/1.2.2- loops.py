# 循环语句示例

# for循环遍历列表
fruits = ['apple', 'banana', 'orange']
for fruit in fruits:
    print(fruit)

# for循环与range()
for i in range(5):
    print(i)

# while循环
count = 0
while count < 5:
    print(f"Count: {count}")
    count += 1

# break和continue
for num in range(10):
    if num == 3:
        continue
    if num == 7:
        break
    print(num)

# 嵌套循环
for i in range(3):
    for j in range(3):
        print(f"({i}, {j})")

# 循环中的else
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(f"{n} = {x} * {n//x}")
            break
    else:
        print(f"{n} 是质数")