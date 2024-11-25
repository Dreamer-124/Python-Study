## 1. 类型注解的使用
```python
def describe_person(name: str, age: int, height: float) -> str:
    return f"{name} is {age} years old and {height}m tall"

print(describe_person("Alice", 25, 1.75))
```
- 程序运行截图
![程序运行截图](practice_1.png)