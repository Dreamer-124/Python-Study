import time

class MyClass:
    def original_method(self):
        return "这是原始方法"

# 定义一个新的方法，用于替换原始方法
def patched_method(self):
    print("开始执行新方法")
    start_time = time.time()
    
    # 调用原始方法
    original_result = original_method_backup(self)
    
    end_time = time.time()
    print("新方法执行完毕")
    print(f"执行时间: {end_time - start_time} 秒")
    
    return original_result

# 备份原始方法
original_method_backup = MyClass.original_method

# 使用猴子补丁替换原始方法
MyClass.original_method = patched_method

# 创建实例并调用被补丁的方法
instance = MyClass()
print(instance.original_method())


