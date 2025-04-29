# 魔术方法示例

class Book:
    """
    图书类，展示魔术方法的使用
    """
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    # __str__ 方法
    def __str__(self):
        return f"《{self.title}》 by {self.author}"
    
    # __len__ 方法
    def __len__(self):
        return self.pages
    
    # __eq__ 方法
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

# 创建对象
book1 = Book("Python编程", "Guido van Rossum", 500)
book2 = Book("Python编程", "Guido van Rossum", 600)

# 测试魔术方法
print(book1)  # 调用 __str__
print(f"页数: {len(book1)}")  # 调用 __len__
print(f"两本书相同吗? {book1 == book2}")  # 调用 __eq__