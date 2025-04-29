import re
from enum import Enum, auto

# re示例
match = re.search(r"(\d+)", "abc123def")
print("找到的数字:", match.group(1))

# enum示例
class Color(Enum):
    RED = auto()
    GREEN = auto()
    BLUE = auto()

print("颜色枚举:", Color.RED)