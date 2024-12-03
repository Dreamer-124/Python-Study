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