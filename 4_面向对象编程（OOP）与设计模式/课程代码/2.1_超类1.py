class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"

class Employee(Person):
    def __init__(self, name: str, age: int, position: str, salary: float):
        super().__init__(name, age)  # 调用父类的初始化函数
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"{super().__str__()}, Position: {self.position}, Salary: {self.salary}"

# 测试代码
employee = Employee("Alice", 30, "Engineer", 80000)
print(employee)  # 输出: Name: Alice, Age: 30, Position: Engineer, Salary: 80000