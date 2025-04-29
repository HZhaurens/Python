# JSON文件处理示例
import json

def write_json(file_path, data):
    """写入JSON文件"""
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def read_json(file_path):
    """读取JSON文件"""
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

# 示例用法
if __name__ == "__main__":
    # 写入JSON文件
    data = {
        "姓名": "张三",
        "年龄": 25,
        "城市": "北京"
    }
    write_json("example.json", data)
    
    # 读取JSON文件
    content = read_json("example.json")
    print(content)