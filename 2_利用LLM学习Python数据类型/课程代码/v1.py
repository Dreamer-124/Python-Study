class Vector:
    def __init__(self, *components):
        self.components = components

    def __add__(self, other):
        return Vector(*(x + y for x, y in zip(self.components, other.components)))

    def __sub__(self, other):
        return Vector(*(x - y for x, y in zip(self.components, other.components)))

    def dot(self, other):
        return sum(x * y for x, y in zip(self.components, other.components))

    def cross(self, other):
        return Vector(self.components[1] * other.components[2] - self.components[2] * other.components[1],
                      self.components[0] * other.components[2] - self.components[2] * other.components[0],
                      self.components[0] * other.components[1] - self.components[1] * other.components[0])

    # 向量乘法
    def __mul__(self, other):
        # 这里假设 * 运算符表示点积
        return self.dot(other)

    def __repr__(self):
        return f"Vector{self.components}"

# 实例化两个向量
vector1 = Vector(1, 2, 3)
vector2 = Vector(4, 5, 6)

# 向量加法
vector3 = vector1 + vector2

# 向量乘法（点积）
vector4 = vector1 * vector2

# 打印向量
print(vector3)  # 输出: Vector(5, 7, 9)
print(vector4)  # 输出: 32