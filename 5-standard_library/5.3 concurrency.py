import threading
import asyncio

# threading示例
def worker():
    print("线程执行")

t = threading.Thread(target=worker)
t.start()
t.join()

# asyncio示例
async def async_task():
    await asyncio.sleep(1)
    print("异步任务完成")

asyncio.run(async_task())