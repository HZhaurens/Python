# Python 所有内置函数示例及详细注释

# abs() 取绝对值
print(abs(-10))  # 输出: 10

# all() 检查所有元素是否为真
print(all([1, 2, 3]))  # 输出: True

# any() 检查是否有元素为真
print(any([0, 0, 3]))  # 输出: True

# ascii() 返回对象的可打印字符串（转义非ASCII字符）
print(ascii('你好'))  # 输出: '\u4f60\u597d'

# bin() 转二进制字符串
print(bin(10))  # 输出: '0b1010'

# bool() 转为布尔值
print(bool(0))  # 输出: False

# breakpoint() 断点调试（Python 3.7+）
# breakpoint()  # 运行到这里会进入调试器

# bytearray() 可变字节数组
ba = bytearray('abc', 'utf-8')
print(ba)  # 输出: bytearray(b'abc')

# bytes() 不可变字节序列
b = bytes('abc', 'utf-8')
print(b)  # 输出: b'abc'

# callable() 判断对象是否可调用
def foo(): pass
print(callable(foo))  # 输出: True

# chr() 整数转字符
print(chr(65))  # 输出: 'A'

# classmethod() 类方法装饰器
class MyClass:
    @classmethod
    def cm(cls):
        return 'class method'
print(MyClass.cm())  # 输出: 'class method'

# compile() 编译代码为代码对象
code = compile('print("hello")', '', 'exec')
exec(code)  # 输出: hello

# complex() 创建复数
print(complex(1, 2))  # 输出: (1+2j)

# delattr() 删除对象属性
class A: x = 1
a = A()
delattr(a, 'x')
print(hasattr(a, 'x'))  # 输出: False

# dict() 创建字典
d = dict(a=1, b=2)
print(d)  # 输出: {'a': 1, 'b': 2}

# dir() 查看对象属性和方法
print(dir([]))  # 输出: list 的所有属性和方法

# divmod() 返回商和余数
print(divmod(10, 3))  # 输出: (3, 1)

# enumerate() 枚举，返回索引和值
for i, v in enumerate(['a', 'b']):
    print(i, v)  # 输出: 0 a 1 b

# eval() 执行字符串表达式
print(eval('1+2'))  # 输出: 3

# exec() 执行字符串代码
exec('x=5')
print(x)  # 输出: 5

# filter() 过滤序列
print(list(filter(lambda x: x > 0, [-1, 0, 1, 2])))  # 输出: [1, 2]

# float() 转为浮点数
print(float('3.14'))  # 输出: 3.14

# format() 格式化字符串
print(format(3.14159, '.2f'))  # 输出: '3.14'

# frozenset() 不可变集合
fs = frozenset([1, 2, 3])
print(fs)  # 输出: frozenset({1, 2, 3})

# getattr() 获取对象属性
class B: y = 10
b = B()
print(getattr(b, 'y'))  # 输出: 10

# globals() 返回全局变量字典
print('globals:', list(globals().keys()))

# hasattr() 判断对象是否有某属性
print(hasattr(b, 'y'))  # 输出: True

# hash() 获取对象哈希值
print(hash('abc'))

# help() 获取帮助信息
# help(str)  # 取消注释可查看帮助

# hex() 转16进制字符串
print(hex(255))  # 输出: '0xff'

# id() 获取对象唯一标识
print(id(b))

# input() 获取用户输入
# s = input('请输入内容:')  # 取消注释可用

# int() 转为整数
print(int('123'))  # 输出: 123

# isinstance() 判断对象类型
print(isinstance(123, int))  # 输出: True

# issubclass() 判断子类关系
print(issubclass(bool, int))  # 输出: True

# iter() 获取迭代器
it = iter([1, 2, 3])
print(next(it))  # 输出: 1

# len() 获取长度
print(len([1, 2, 3]))  # 输出: 3

# list() 创建列表
print(list((1, 2, 3)))  # 输出: [1, 2, 3]

# locals() 返回局部变量字典
def test_locals():
    a = 1
    print(locals())
test_locals()

# map() 映射
print(list(map(str, [1, 2, 3])))  # 输出: ['1', '2', '3']

# max() 最大值
print(max([1, 2, 3]))  # 输出: 3

# memoryview() 内存视图对象
mv = memoryview(b'abc')
print(mv[0])  # 输出: 97

# min() 最小值
print(min([1, 2, 3]))  # 输出: 1

# next() 获取迭代器下一个元素
it2 = iter([4, 5])
print(next(it2))  # 输出: 4

# object() 创建空对象
o = object()
print(type(o))  # 输出: <class 'object'>

# oct() 转8进制字符串
print(oct(8))  # 输出: '0o10'

# open() 打开文件
# with open('test.txt', 'w') as f:
#     f.write('hello')

# ord() 字符转整数
print(ord('A'))  # 输出: 65

# pow() 幂运算
print(pow(2, 3))  # 输出: 8

# print() 打印
print('Hello, world!')

# property() 属性装饰器
class C:
    def __init__(self):
        self._x = 1
    @property
    def x(self):
        return self._x
c = C()
print(c.x)  # 输出: 1

# range() 生成范围序列
print(list(range(3)))  # 输出: [0, 1, 2]

# repr() 获取对象字符串表示
print(repr('abc'))  # 输出: "'abc'"

# reversed() 反转序列
print(list(reversed([1, 2, 3])))  # 输出: [3, 2, 1]

# round() 四舍五入
print(round(3.14159, 2))  # 输出: 3.14

# set() 创建集合
print(set([1, 2, 2, 3]))  # 输出: {1, 2, 3}

# setattr() 设置对象属性
setattr(b, 'z', 99)
print(b.z)  # 输出: 99

# slice() 切片对象
s = slice(1, 3)
print([0, 1, 2, 3][s])  # 输出: [1, 2]

# sorted() 排序
print(sorted([3, 1, 2]))  # 输出: [1, 2, 3]

# staticmethod() 静态方法装饰器
class D:
    @staticmethod
    def sm():
        return 'static method'
print(D.sm())  # 输出: 'static method'

# str() 转为字符串
print(str(123))  # 输出: '123'

# sum() 求和
print(sum([1, 2, 3]))  # 输出: 6

# super() 调用父类方法
class E:
    def hello(self):
        return 'hello'
class F(E):
    def hello(self):
        return super().hello() + ' world'
f = F()
print(f.hello())  # 输出: 'hello world'

# tuple() 创建元组
print(tuple([1, 2, 3]))  # 输出: (1, 2, 3)

# type() 获取类型
print(type(123))  # 输出: <class 'int'>

# vars() 返回对象的__dict__属性
print(vars(b))  # 输出: b对象的属性字典

# zip() 打包为元组
print(list(zip([1, 2], ['a', 'b'])))  # 输出: [(1, 'a'), (2, 'b')]

# __import__() 动态导入模块
math = __import__('math')
print(math.sqrt(16))  # 输出: 4.0