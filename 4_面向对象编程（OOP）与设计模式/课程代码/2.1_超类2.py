from collections import UserDict

class LoggingDict(UserDict):
    def __setitem__(self, key, value):
        print(f"Setting {key} to {value}")
        super().__setitem__(key, value)  # 调用父类的 __setitem__ 方法

class ValidatedDict(LoggingDict):
    def __setitem__(self, key, value):
        if not isinstance(key, str):
            raise TypeError("Key must be a string")
        if not isinstance(value, int):
            raise TypeError("Value must be an integer")
        super().__setitem__(key, value)  # 调用父类的 __setitem__ 方法


# 测试代码
validated_dict = ValidatedDict()
validated_dict["age"] = 30  # 输出: Setting age to 30
print(validated_dict)  # 输出: {'age': 30}

# 尝试设置无效的键值对
try:
    validated_dict[10] = "thirty"
except TypeError as e:
    print(e)  # 输出: Key must be a string