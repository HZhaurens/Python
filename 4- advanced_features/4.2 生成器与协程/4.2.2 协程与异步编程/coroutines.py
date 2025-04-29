"""
协程示例
====================

本模块演示协程的基本用法:

1. 协程的定义与使用
2. 协程与生成器的区别
"""

import asyncio

# 简单协程示例
async def simple_coroutine():
    """简单协程函数"""
    print("协程开始执行")
    await asyncio.sleep(1)
    print("协程执行完成")

# 协程调用
def run_coroutine():
    """运行协程"""
    asyncio.run(simple_coroutine())

if __name__ == "__main__":
    print("协程示例:")
    run_coroutine()