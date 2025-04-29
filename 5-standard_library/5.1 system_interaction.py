import os
import sys
import argparse
import subprocess

# os示例
print("当前工作目录:", os.getcwd())
os.makedirs("temp_dir", exist_ok=True)

# sys示例
print("命令行参数:", sys.argv)
print("Python路径:", sys.path)

# argparse示例
parser = argparse.ArgumentParser()
parser.add_argument("--input", help="输入文件")
args = parser.parse_args()

# subprocess示例
result = subprocess.run(["echo", "Hello"], capture_output=True, text=True)
print("子进程输出:", result.stdout)