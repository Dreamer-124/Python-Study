import functools

# 类装饰器：缓存机制
class CacheDecorator:
    def __init__(self, cls):
        self.cls = cls
        self.cache = {}

    def __call__(self, *args, **kwargs):
        key = (args, tuple(kwargs.items()))
        if key not in self.cache:
            self.cache[key] = self.cls(*args, **kwargs)
        return self.cache[key]

@CacheDecorator
class RetrievalComponent:
    def retrieve(self, query: str) -> str:
        # 模拟检索操作
        return f"Results for {query}"

# 描述符：类型检查和访问控制
class TypeCheckedAttribute:
    def __init__(self, name, expected_type):
        self.name = name
        self.expected_type = expected_type

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError(f"Expected {self.expected_type} for {self.name}, got {type(value)}")
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        raise AttributeError(f"Cannot delete attribute {self.name}")

class DataComponent:
    data = TypeCheckedAttribute("data", str)

    def __init__(self, data):
        self.data = data

# 测试代码
def main():
    # 测试类装饰器
    retrieval_component = RetrievalComponent()
    print(retrieval_component.retrieve("query1"))  # 输出: Results for query1
    print(retrieval_component.retrieve("query1"))  # 输出: Results for query1（从缓存中获取）

    # 测试描述符
    data_component = DataComponent("valid data")
    print(data_component.data)  # 输出: valid data

    try:
        data_component.data = 123  # 触发类型检查错误
    except TypeError as e:
        print(e)  # 输出: Expected <class 'str'> for data, got <class 'int'>

if __name__ == "__main__":
    main()