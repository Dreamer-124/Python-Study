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
    
# 实现多轮对话
# 最多只保留 5 轮对话
# 创建一个大小只能容纳 5 个元素的集合
history = set(maxlen=5)

if len(history) == 5:
    history.pop()
history.add(input("请输入对话内容："))

    
if __name__ == "__main__":
    v1 = Vector([1, 2, 3, 4])
    v2 = Vector([2, 3, 4, 5])
    print(v1 + v2)
    print(v1 * v2)
