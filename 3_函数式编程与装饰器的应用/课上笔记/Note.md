## 1. 借助 LLM 正确理解函数的概念
### 1.1 函数的概念
- `Python`函数的特点
  - 在运行时创建
  - 能赋值给变量或数据结构中的元素
  - 能作为参数传递给函数
  - 能作为函数的返回结果
- `callable()`是检测函数的最普遍和最安全方式
```python
# 定义一个简单函数，并添加文档字符串
def sample_function():
    """
    这是一个示例函数。
    """
    pass

# 编写测试函数
def test_function_doc_and_type():
    # 读取函数的__doc__属性
    doc = sample_function.__doc__
    # 检查函数类型
    func_type = type(sample_function)
    try:
        # 断言文档字符串是否正确
        assert doc == "\n    这是一个示例函数。\n    ", f"文档字符串不匹配: {doc}"
        print("文档字符串匹配")
    except AssertionError as e:
        print(e)
    try:
        # 断言函数类型是否为funciton
        assert func_type == type(lambda: None), f"函数类型不匹配: {func_type}"
        print("函数类型匹配")
    except AssertionError as e:
        print(e)


# 使用 unittest 模块编写单元测试
import unittest

class TestSampleFunction(unittest.TestCase):
    def test_doc(self):
        self.assertEqual(sample_function.__doc__, "\n    这是一个示例函数。\n    ")
    
    def test_type(self):
        self.assertTrue(callable(sample_function))
        self.assertEqual(type(sample_function), type(lambda: None))


if __name__ == "__main__":
    test_function_doc_and_type()  # 调用测试函数
    unittest.main()  # 调用 unittest.main() 运行测试用例
```
- 在`SQLQueryBuilder`类中实现`__call__`方法，该方法接受查询参数并返回完整的`SQL`查询字符串
```python
class SQLQueryBuilder:
    def __init__(self, base_query):
        self.base_query = base_query
    
    def __call__(self, **kwargs):
        query = self.base_query
        for key, value in kwargs.items():
            placeholder = f"{{{key}}}"
            query = query.replace(placeholder, str(value))
        return query
    

# 创建 SQLQueryBuilder 实例
base_query = "SELECT * FROM users WHERE age > {age} AND city = '{city}'"
query_builder = SQLQueryBuilder(base_query)

# 像调用函数一样调用该实例来生成不同的 SQL 查询
query1 = query_builder(age = 30, city = "New York")
query2 = query_builder(age = 25, city = "San Francisco")

print(query1)
print(query2)
```
- 在`python`中，会将定义态与执行态分开来写

### 1.2 匿名函数
- 使用`lambda`关键字，可以在`python`中创建匿名函数，即没有明确名称的函数
- 由于`python`语法的简化，`lambda`函数的主体只能包含表达式，不能包含循环、异常处理等语句
- `lambda`函数的复杂性可能导致代码可读性下降，因此建议将复杂逻辑重构为使用`def`定义的常规函数，以提高代码的可维护性和可读性
```python
# 1. 计算两个数的加权平均值的 lambda 表达式
weight_average_lambda = lambda x, y, wx, wy: (x * wx + y * wy) / (wx + wy)
print(weight_average_lambda(3, 5, 0.4, 0.6))

# 2. 过滤列表中所有大于某个值且是偶数的 lambda 表达式
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
threshold = 5
filtered_numbers = list(filter(lambda x: x > threshold and x % 2 == 0, numbers))
print(filtered_numbers)
```

### 1.3 可调用对象
- 内置函数：使用`C`语言`(C Python)`实现的函数，例如：`len`或`time.strftime`
- 用户定义的函数：使用`def`语句或者`lambda表达式`创建的函数 
- 内置方法：使用`C`语言实现的方法，例如：`dict.get`
- 方法：在类主体中定义的函数
- 类：调用类时运行类的`__new__`方法创建一个实例，然后运行__init__方法，初始化实例，然后再把实例返回给调用方，`Python`中没有`new`运算符，调用类就相当于调用函数
- 类的实例：如果类定义了`__call__`方法，那么它的实例可以作为函数调用
- 生成器函数：主体中有`yield`关键字的函数或方法，调用生成器函数返回一个生成器对象
- 原生协程函数：使用`async def`定义的函数或方法，调用原生协程函数返回一个协程对象
- 异步生成器函数：使用`async def`定义，而且主体中有`yield`关键字的函数或方法。调用异步生成器函数返回一个异步生成器，供`async for`使用

### 1.4 函数式编程
- 柯里化（currying）：在`Python`中，`functools.partial`函数可以用于函数柯里化。柯里化是一种将接收多个参数转换为接收单一参数（返回接收余下参数的新函数）的技术，`partial`函数通过固定函数的部分参数并返回一个新的函数来实现这一点
- 使用`partial`进行函数柯里化示例
```python
# 假设我们有一个简单的函数 add，它接收两个参数并返回它们的和：
def add(x, y):
    return x + y

# 我们可以使用 partial 函数将其柯里化：
from functools import partial

# 创建一个新的函数 add_one，它将 x 固定为 1
add_one = partial(add, 1)

# 调用 add_one 函数，只需要传递 y 参数
result = add_one(2)  # 相当于调用 add(1, 2)
print(result)  # 输出 3
```

## 2. 借助 LLM 掌握装饰器的概念
### 2.1 装饰器的概念
- 定义：装饰器是可调用的对象之一，装饰器的参数是另一个函数对象，装饰器会对被装饰的函数做处理，然后返回函数（对象），或者把函数替换成另一个函数或可调用对象
- 误区：装饰器不是是装饰设计模式，装饰器是对被装饰函数的扩展，可以改变原工作模式，装饰器不是在调用时才运行（实际上，装饰器是在被装饰的函数定义后立即运行，如果函数从其他模块导入，则导入时立即执行）

### 2.2 闭包与装饰器
- 变量作用域查找规则`LEGB` 
- 闭包：闭包是指在函数内部定义的函数可以访问其外部函数的变量，即使外部函数已经执行完毕。闭包是的函数可以记住其创建时的环境
- 闭包可以用来解决哪些编程问题？：数据封装、回调函数、工厂函数、保持现状
- 数据封装：闭包可以将数据封装在函数内部，提供一种私有变量的机制，防止外部直接访问和修改
```python
def make_counter():
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter

counter = make_counter()
print(counter())
print(counter())
```
- 回调函数：闭包可以用来创建回调函数，特别是在异步编程或事件驱动编程中
```python
def create_callback(message):
    def callback():
        print(message)
    return callback

callback = create_callback("Hello, World!")
callback()

```
- 工厂函数：闭包可以用来创建工厂函数，根据不同的参数生成不同的函数
```python
def power_factory(exp):
    def power(base):
        return base ** exp
    return power

square = power_factory(2)
cube = power_factory(3)

print(square(2))
print(cube(2))
```
- 保持状态：闭包可以用来保持函数调用之间的状态，而不需要使用全局变量或类
```python
def make_accumulator():
    total = 0
    def accumulator(value):
        nonlocal total
        total += value
        return total
    return accumulator

acc = make_accumulator()
print(acc(10))
print(acc(5))
```
- 装饰器：闭包是实现装饰器的基础，可以在不修改原函数的情况下扩展其功能
```python
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args} and {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@logger
def add(x, y):
    return x + y

print(add(1, 2))
```

## 3. 借助 LLM 掌握装饰器的用法
### 3.1 常见的装饰器用法
- 装饰器的参数
```python
# 装饰器的参数处理
class AAA:
    def bbb(self, ccc):
        def decorator(func):
            def wrapper(*args, **kwargs):
                print(f"Dectorator parameter: {ccc}")
                print("Before function call")
                result = func(*args, **kwargs)
                print("After function call")
                return result
            return wrapper
        return decorator

# 实例化类
aaa = AAA()

# 使用装饰器
@aaa.bbb("example parameter")
def my_function():
    print("Inside my_function")

# 调用函数
my_function()

# AAA 类包含一个方法 bbb，该方法接受一个参数 ccc。
# bbb 方法返回一个装饰器 decorator，该装饰器接受一个函数 func 作为参数。
# decorator 返回一个新的函数 wrapper，该函数在调用 func 之前和之后执行一些操作。
# @aaa.bbb("example parameter") 使用 AAA 类的实例 aaa 调用 bbb 方法，并传递参数 "example parameter"，从而应用装饰器。

```
- 装饰器的叠放
 - `log_execution`装饰器记录函数的执行日志
 - `measure_time`装饰器测量函数的执行时间
 - 这些装饰器被叠放在`InMemoryCache`类的方法上，以便在方法执行时同时记录日志和测量时间
 ```python
 # langchain cache.py
# 定义两个装饰器 log_execution 和 measure_time
# 在 InMemoryCache 类的方法上叠放这两个装饰器
import time
from typing import Any, Callable, Dict, Optional, Tuple, TypeVar
from functools import wraps

RETURN_VAL_TYPE = TypeVar("RETURN_VAL_TYPE")

def log_execution(func: Callable) -> Callable:
    """Decorator to log the execution of a function."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Executing {func.__name__} with args: {args} and kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"Finished executing {func.__name__}")
        return result
    return wrapper

def measure_time(func: Callable) -> Callable:
    """Decorator to measure the execution time of a function."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time} seconds to execute")
        return result
    return wrapper

class InMemoryCache:
    """Cache that stores things in memory."""

    def __init__(self) -> None:
        """Initialize with empty cache."""
        self._cache: Dict[Tuple[str, str], RETURN_VAL_TYPE] = {}

    @log_execution
    @measure_time
    def lookup(self, prompt: str, llm_string: str) -> Optional[RETURN_VAL_TYPE]:
        """Look up based on prompt and llm_string."""
        return self._cache.get((prompt, llm_string), None)
    
    @log_execution
    @measure_time
    def update(self, prompt: str, llm_string: str, return_val: RETURN_VAL_TYPE) -> None:
        """Update the cache based on prompt and llm_string."""
        self._cache[(prompt, llm_string)] = return_val

    @log_execution
    @measure_time
    def clear(self, **kwargs: Any) -> None:
        """Clear cache."""
        self._cache = {}

    @log_execution
    @measure_time
    async def alookup(self, prompt: str, llm_string: str) -> Optional[RETURN_VAL_TYPE]:
        """Look up based on prompt and llm_string."""
        return self._cache.get((prompt, llm_string))
    
    @log_execution
    @measure_time
    async def aupdate(self, prompt: str, llm_string: str, return_val: RETURN_VAL_TYPE) -> None:
        """Update cache based on prompt and llm_string."""
        self.update(prompt, llm_string, return_val)

    @log_execution
    @measure_time
    async def aclear(self, **kwargs: Any) -> None:
        """Clear cache."""
        self.clear()
 ```
- 保持函数签名
```python
# 使用 @wraps(func) 保持函数签名
def log_execution(func: callable) -> Callable:
    """Decorator to log function execution time."""
    @wraps(func)
```

### 3.2 LLM 中如何使用装饰器
- `@property`和`@similarity_top_k.setter`：用于将方法转换为属性，并定义属性的获取和设置行为
```python 
# llama_index retriever.py
@property
def similarity_top_k(self) -> int:
    """Return similarity top k."""
    return self._similarity_top_k

@similarity_top_k.setter    
def similarity_top_k(self, similarity_top_k: int):
    """Set similarity top k."""
    self._similarity_top_k = similarity_top_k
```
- `langchain`的`model_validator`装饰器的作用：
 - `model_validator`装饰器用于在模型的生命周期中执行验证逻辑。它可以在模型的某个操作之前或之后执行特定的验证代码
 - 使用方法：`model_validator(model = "before")`：在某个操作之前验证 `model_validator(model = "after")`：在某个操作之后进行验证
```python 
@model_validator(model = "before")
@classmethod
def validate_enviroment(cls, values: Dict) -> Any:
    pass

@model_validator(model = "after")
def post_init(self) -> Self:
    pass
```
- 更加复杂的使用方法，这些装饰器结合在一起，确保只有经过身份验证的用户才能发送包含`doc_id`和`content_with_weight`字段的`POST`请求到`/create`路径，并由`create`函数处理。
```python
@manager.route('/create', methods=['POST'])
@login_required
@validate_request("doc_id", "content_with_weight")
def create():
    req = request.json
    md5 = hashlib.md5()
    md5.update(req["content_with_weight"] + req["doc_id"]).encode("utf-8")
    chunk_id = md5.hexdigest()
```
- `RagFlow`中的`knowledgebase_service.py`
 - `@DB.connection_context()`用于在函数执行前后自动管理数据库连接的打开和关闭
 - 当`get_list`方法被调用时，`DB.connection_context()`装饰器会首先打开一个数据库连接
 - `get_list`方法在这个连接上下文中执行
 - 方法执行完毕后，装饰器会自动关闭数据库连接
```python
@classmethod
@DB.connection_context()
def get_list(cls, joined_tenant_ids, user_id,
             page_number, items_per_page, orderby, desc, id, name):
    kbs = cls.model
    pass
```