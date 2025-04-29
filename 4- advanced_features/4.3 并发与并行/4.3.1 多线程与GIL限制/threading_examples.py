"""
多线程与GIL限制示例
====================

本模块演示Python中多线程与GIL限制的基本用法:

1. 多线程创建与启动
2. GIL对多线程性能的影响
"""

import threading
import time

# 简单线程示例
def worker(num):
    print(f"线程{num}开始执行")
    time.sleep(1)
    print(f"线程{num}执行完成")

# 多线程创建
def create_threads():
    threads = []
    for i in range(3):
        t = threading.Thread(target=worker, args=(i,))
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()

# GIL限制示例
count = 0

def increment_count():
    global count
    for _ in range(1000000):
        count += 1

# 多线程计数
def test_gil_impact():
    global count
    count = 0
    
    t1 = threading.Thread(target=increment_count)
    t2 = threading.Thread(target=increment_count)
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    
    print(f"最终计数结果: {count}")

if __name__ == "__main__":
    print("简单线程示例:")
    create_threads()
    
    print("\nGIL限制示例:")
    test_gil_impact()