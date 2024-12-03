## 1. 契约式设计与防御式编程的实践
### 1.1 契约式设计
- 为什么要写整洁的代码：编程语言中的语言是开发人员用于彼此交流想法的途径
- 技术债务：技术债务指的是因妥协或糟糕的决策导致的软件问题
- 契约式设计（Design by Contract，DbC）是一种软件设计方法，旨在通过明确的契约（合同）来定义软件组织之间的交互，契约包括前置条件、后置条件和不变量，确保组件在特定条件下正确运行
- 契约式设计的核心概念
    - 前置条件（Preconditions）：在调用方法或函数之前必须满足的条件
    - 后置条件（Postconditions）：在方法或函数执行完毕后必须满足的条件
    - 不变量（Invariants）；在对象的生命周期内始终保持为真的条件
- 实现方法：
    - 明确模块间的接口契约，使用断言和异常确保契约不被破坏
- 使用装饰器来实现前置条件和后置条件
```python
from functools import wraps

def precondition(predicate):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            assert predicate(*args, **kwargs), f"Precondition failed for {func.__name__}"
            return func(*args, **kwargs)
        return wrapper
    return decorator

def postcondition(predicate):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            assert predicate(result), f"Postcondition failed for {func.__name__}"
            return result
        return wrapper
    return decorator

# 示例类
class Account:
    def __init__(self, balance):
        self.balance = balance

    @precondition(lambda self, amount: amount > 0)
    @postcondition(lambda result: result is True)
    def deposit(self, amount):
        self.balance += amount
        return True

    @precondition(lambda self, amount: 0 < amount <= self.balance)
    @postcondition(lambda result: result is True)
    def withdraw(self, amount):
        self.balance -= amount
        return True

# 测试代码
account = Account(100)
account.deposit(50)  # 成功
account.withdraw(30)  # 成功

try:
    account.withdraw(150)  # 失败，前置条件不满足
except AssertionError as e:
    print(e)  # 输出: Precondition failed for withdraw
```
- 使用上下文管理器来确保不变量在对象的生命周期内保持为真
```python
class Invariant:
    def __init__(self, predicate):
        self.predicate = predicate
    
    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        assert self.predicate(), 'Invariant condition failed'


# 示例类
class Account:
    def __init__(self, balance):
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        self.balance -= amount

    def check_invariant(self):
        return self.balance >= 0


# 测试代码
account = Account(100)
with Invariant(account.check_invariant):
    account.deposit(50)
    account.withdraw(30)

try:
    with Invariant(account.check_invariant):
        account.withdraw(150)  # 失败，不变量不满足
except AssertionError as e:
    print(e)  # 输出：Invariant condition failed
        
```

### 1.2 防御式编程
- 实现方法：防御式编程是一种编程实践，通过在关键路径添加输入验证和错误处理，防止异常传播，从而提高软件的可靠性和可维护性
- 如何使用装饰器统一实现输入验证逻辑，并包括错误处理（如值替换和异常处理）以及断言
- 定义装饰器用于输入验证和错误处理
```python
from functools import wraps

def validate_inputs(validation_func):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if not validation_func(*args, **kwargs):
                raise ValueError(f"Input validation failed for {func.__name__}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

def handle_errors(default_value = None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print(f"Error in {func.__name__}: {e}")
                return default_value
        return wrapper
    return decorator

```
- 定义一个示例类，使用装饰器进行输入验证和错误处理
```python
from functools import wraps


def validate_inputs(validation_func):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if not validation_func(*args, **kwargs):
                raise ValueError(f"Input validation failed for {func.__name__}")
            return func(*args, **kwargs)
        return wrapper
    return decorator


def handle_errors(default_value = None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print(f"Error in {func.__name__}: {e}")
                return default_value
        return wrapper
    return decorator


class Calculator:
    @validate_inputs(lambda self, x, y: isinstance(x, (int, float)) and isinstance(y, (int, float)))
    @handle_errors(default_value = 0)
    def add(self, x, y):
        return x + y
    
    @validate_inputs(lambda self,x, y: isinstance(x, (int, float)) and isinstance(y, (int, float)) and y != 0)
    @handle_errors(default_value = float("inf"))
    def divide(self, x, y):
        return x / y


# 测试代码
calc = Calculator()

# 正常操作
print(calc.add(1, 2))  # 3
print(calc.divide(1, 2))  # 0.5

# 输入验证失败
try:
    print(calc.add(1, "2"))
except ValueError as e:
    print(e)  # Input validation failed for add

# 错误处理
try:
    print(calc.divide(1, 0))
except Exception as e:
    print(e)
```
