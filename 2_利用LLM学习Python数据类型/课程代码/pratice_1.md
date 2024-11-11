## 1.1
- 不借助 LLM 如何构造两个向量，如何编写运算方法
```Python
X = [1, 2, 3, 4]
Y = [2, 3, 4, 5]
Z = [0, 0, 0, 0]
W = 0
for i in range(len(X)):
Z[i] = X[i] + Y[i]

for i in range(len(X)):
W += X[i] * Y[i]
print(Z, W)
``` 

## 1.2
- 通过注释，让 LLM 补全代码，实现向量运算
```Python
# -*- coding: utf-8 -*-

# 实现两个向量的加法
def vector_add(X, Y):
result = []
for x, y in zip(X, Y):
    result.append(x + y)
return result

# 实现两个向量的乘法
def vector_multiply(X, Y):
result = 0
for x, y in zip(X, Y):
    result += x * y
return result

if __name__ == "__main__":
# 定义两个向量
X = [1, 2, 3, 4]
Y = [2, 3, 4, 5]

print(vector_add(X, Y), vector_multiply(X, Y))
```

## 1.3
- 通过Chat方式生成代码，比较注释方式，哪种效果更好。
```Python
# 实现两个向量的加法
def vector_add(X, Y):
result = []
for x, y in zip(X, Y):
    result.append(x + y)
return result

# 实现两个向量的乘法
def vector_multiply(X, Y):
result = 0
for x, y in zip(X, Y):
    result += x * y
return result

if __name__ == "__main__":
# 定义两个向量
X = [1, 2, 3, 4]
Y = [2, 3, 4, 5]

# 输出加法和乘法的结果
print("向量加法结果:", vector_add(X, Y))
print("向量乘法结果:", vector_multiply(X, Y))
```

## 1.4
- 最终优化版
```Python
# 创建一个实例化向量对象的类
class Vector:
def __init__(self, data):
    self.data = data

def __repr__(self):
    return f"Vector({self.data})"

# 实现两个向量的加法
def __add__(self, other):
    return Vector([x + y for x, y in zip(self.data, other.data)])

# 实现两个向量的乘法
def __mul__(self, other):
    return sum([x * y for x, y in zip(self.data, other.data)])

if __name__ == "__main__":
v1 = Vector([1, 2, 3, 4])
v2 = Vector([2, 3, 4, 5])
print(v1 + v2)
print(v1 * v2)
```