## 4. 设计一个装饰器来记录函数的调用次数，并且在调用次数达到一定阈值时，通知用户并让程序正常停止
```python
from functools import wraps

def call_limiter(max_calls):
    def decorator(func):
        call_count = 0  # 用于记录函数调用次数的变量
        @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal call_count  # 使用 nonlocal 关键字来修改外部函数的变量
            call_count += 1  # 每次调用函数时，调用次数加一
            if call_count > max_calls:
                print(f"Function '{func.__name__}' has been called {max_calls} times. Stopping execution.")
                return  # 达到阈值，停止执行
            result = func(*args, **kwargs)  # 调用原始函数
            return result  # 返回原始函数的结果
        return wrapper
    return decorator

# 使用示例
@call_limiter(3)
def greet(name):
    print(f"Hello, {name}!")

# 测试装饰器
greet("Alice")  # 正常调用
greet("Bob")    # 正常调用
greet("Charlie")  # 正常调用，达到阈值，打印消息并停止
greet("Dave")    # 这行不会被执行
```