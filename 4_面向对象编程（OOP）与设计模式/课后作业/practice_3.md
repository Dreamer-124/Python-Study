## 3. 猴子补丁
```python
# 原始方法
class ExternalClass:
    def calculate(self, x, y):
        print("原始方法")
        return x * y  # 应当更改为 x + y

# 猴子补丁
def monkey_patch(self, x, y):
    print("更换成新方法")
    return x + y


# 测试代码
myclass = ExternalClass()
print(myclass.calculate(2, 3))

ExternalClass.calculate = monkey_patch
myclass = ExternalClass()
print(myclass.calculate(2, 3))
```
- 程序运行截图
![程序运行截图](practice_3.png)
