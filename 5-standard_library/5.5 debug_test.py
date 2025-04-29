import logging
import unittest

# logging示例
logging.basicConfig(level=logging.INFO)
logging.info("这是一条信息日志")

# unittest示例
class TestExample(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(1 + 1, 2)

if __name__ == "__main__":
    unittest.main()