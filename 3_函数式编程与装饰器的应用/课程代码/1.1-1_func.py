# 定义一个简单的函数，并添加文档字符串
def sample_function():
    """
    这是一个示例函数。
    """
    pass

# 编写测试函数
def test_function_doc_and_type():
    # 读取函数的__doc__属性
    doc = sample_function.__doc__
    # 检查函数的类型
    func_type = type(sample_function)
    try:
        # 断言文档字符串是否正确
        assert doc == "\n    这是一个示例函数。\n    ", f"文档字符串不匹配: {doc}"
        print("文档字符串匹配")
    except AssertionError as e:
        print(e)
    try:
        # 断言函数类型是否为function
        assert func_type == type(lambda: None), f"函数类型不匹配: {func_type}"
        print("函数类型匹配")
    except AssertionError as e:
        print(e)

# 使用unittest模块编写单元测试
import unittest

class TestSampleFunction(unittest.TestCase):
    def test_doc(self):
        self.assertEqual(sample_function.__doc__, "\n    这是一个示例函数。\n    ")
    def test_type(self):
        self.assertTrue(callable(sample_function))
        self.assertEqual(type(sample_function), type(lambda: None))

if __name__ == "__main__":
    test_function_doc_and_type()  # 调用测试函数
    unittest.main()
