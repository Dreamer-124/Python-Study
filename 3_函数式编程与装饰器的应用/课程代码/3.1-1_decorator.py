# 装饰器的参数处理
class AAA:
    def bbb(self, ccc):
        def decorator(func):
            def wrapper(*args, **kwargs):
                print(f"Decorator parameter: {ccc}")
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