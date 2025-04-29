from collections import defaultdict, Counter
import itertools

# collections示例
d = defaultdict(int)
d["a"] += 1
print("默认字典:", d)

counts = Counter("abracadabra")
print("字符计数:", counts)

# itertools示例
for i in itertools.islice(itertools.count(), 5):
    print("迭代器:", i)