# 任务一 Python 的鸭子类型与魔术方法
## 1. 借助文档与 LLM 回顾 Python 内置数据类型
### 1.1 如何理解 Python 和它的数据类型
- Python 是一个框架，数据模型就是框架的接口，数据模型包含了序列、映射、集合、函数、类、迭代器等，其中内置的数据类型就是最简单的数据模型，以处理JSON数据为例
```Python
import json

# 一个字典
data = {
    "name": "John Doe",
    "age": 30,
    "address": {
        "street": "123 Main St",
        "city": "Anytown",
        "state": "CA",
        "postalCode": "12345"
    },
    "phoneNumbers": [
        {"type": "home", "number": "555-555-5555"},
        {"type": "work", "number": "555-555-5556"}
    ],
    "children": [
        {"name": "Jane Doe", "age": 10},
        {"name": "Jim Doe", "age": 8}
    ],
    "spouse": None
}

# 将字典转换为 JSON 字符串
json_str = json.dumps(data, indent=4)
print("JSON 字符串:")
print(json_str)


# 直接处理 Python 字典
print("\n直接处理 Python 字典:")
print(f"姓名: {data['name']}")
print(f"地址: {data['address']['street']}, {data['address']['city']}, {data['address']['state']} {data['address']['postalCode']}")
print(f"第一个电话号码: {data['phoneNumbers'][0]['number']}")

# 直接从 JSON 字符串中提取第二个电话号码
second_phone_number = json.loads(json_str)["phoneNumbers"][1]["number"]
print("从 JSON 字符串中提取的第二个电话号码:")
print(second_phone_number)

# 直接从 Python 字典中提取第二个电话号码
second_phone_number_dict = data["phoneNumbers"][1]["number"]
print("\n从 Python 字典中提取的第二个电话号码:")
print(second_phone_number_dict)
```

### 1.2 标准答案：Python 文档
- [标准库和内置类型](https://docs.python.org/zh-cn/3.10/library/index.html#library-index)

### 1.3 如何借助 LLM 掌握数据类型和它的内置方法
- 使用通用序列操作完成对一定数据类型的处理，例如：使用 len() 函数获取列表、元组、字典的长度
```Python
# 创建一个列表、元组、字典
my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)
my_dict = {'a': 1, 'b': 2, 'c': 3}

# 使用 len() 函数获取列表、元组、字典的长度
print(f"列表的长度为：{len(my_list)}")
print(f"元组的长度为：{len(my_tuple)}")
print(f"字典的长度为：{len(my_dict)}")  
```
- len() 函数对应的魔术方法是 `__len__()`。当调用 len() 函数时，Python 解释器会调用对象的 `__len__()` 方法，并返回方法的返回值。
```Python
class MyCollection:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)

# 创建一个自定义集合对象
my_collection = MyCollection([1, 2, 3, 4, 5])

# 使用 len() 函数获取自定义集合对象的长度
print(f"自定义集合的长度为：{len(my_collection)}")
```

### 1.4 学会数据类型和内置方法的目的
- 提高代码效率：
    - 使用内置方法可以利用Python提供高效的实现，避免重复造轮子
    - 了解数据类型的特性和方法，可以选择最合适的数据结构，从而提高代码的性能
- 增强代码可读性和可维护性：
    - 使用内置方法和魔术方法可以使代码更简洁、易读
    - 通过使用标准的Python方法和约定，其他开发者更容易理解和维护代码
- 提高代码的灵活性和可扩展性：
    - 通过实现魔术方法，可以自定义对象的行为，使其与内置类型和函数兼容
    - 这使得自定义对象可以像内置对象一样使用，从而提高代码的灵活性和可扩展性
```Python
class MyCollection:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, value):
        self.items[index] = value

    def __delitem__(self, index):
        del self.items[index]

    def __iter__(self):
        return iter(self.items)

# 创建一个自定义集合对象
my_collection = MyCollection([1, 2, 3, 4])

# 使用内置方法和魔术方法
print(f"集合的长度: {len(my_collection)}")
print(f"第一个元素: {my_collection[0]}")
my_collection[1] = 5
print(f"修改后的集合: {my_collection.items}")
del my_collection[2]
print(f"删除元素后的集合: {my_collection.items}")

# 迭代集合
for item in my_collection:
    print(item)
```
