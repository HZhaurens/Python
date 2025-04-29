# CSV文件处理示例
import csv

def read_csv(file_path):
    """读取CSV文件内容"""
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        return [row for row in reader]

def write_csv(file_path, data):
    """写入CSV文件内容"""
    with open(file_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)

# 示例用法
if __name__ == "__main__":
    # 写入CSV文件
    data = [
        ['姓名', '年龄', '城市'],
        ['张三', '25', '北京'],
        ['李四', '30', '上海']
    ]
    write_csv("example.csv", data)
    
    # 读取CSV文件
    content = read_csv("example.csv")
    for row in content:
        print(row)