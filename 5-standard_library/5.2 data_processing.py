from pathlib import Path
import shutil
import json

# pathlib示例
p = Path("test.txt")
p.write_text("测试内容")
print("文件内容:", p.read_text())

# shutil示例
shutil.copy("test.txt", "test_copy.txt")

# json示例
data = {"name": "John", "age": 30}
json.dump(data, open("data.json", "w"))
loaded = json.load(open("data.json"))
print("加载的JSON:", loaded)