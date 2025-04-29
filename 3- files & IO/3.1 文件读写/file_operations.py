# 基本文件操作示例

def read_file(file_path):
    """读取文件内容"""
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(file_path, content):
    """写入文件内容"""
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

def append_file(file_path, content):
    """追加文件内容"""
    with open(file_path, 'a', encoding='utf-8') as f:
        f.write(content)

# 示例用法
if __name__ == "__main__":
    # 写入文件
    write_file("example.txt", "这是第一行内容\n")
    # 追加内容
    append_file("example.txt", "这是追加的内容\n")
    # 读取文件
    content = read_file("example.txt")
    print(content)