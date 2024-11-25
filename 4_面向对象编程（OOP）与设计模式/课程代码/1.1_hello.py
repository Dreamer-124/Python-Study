# 我们创建一个 Employee 类来代表公司员工，包含基本的员工信息和计算年度薪资的方法。

class Employee:
    # 类变量：用于统计员工人数（体现静态属性）
    employee_count = 0

    def __init__(self, name, position, salary):
        """
        初始化员工的基本信息。
        :param name: 员工姓名
        :param position: 员工职位
        :param salary: 每月薪资（假设以美元计）
        """
        self.name = name  # 员工姓名（实例变量）
        self.position = position  # 员工职位（实例变量）
        self.salary = salary  # 每月薪资（实例变量）
        
        # 每创建一个新员工实例，员工人数+1
        Employee.employee_count += 1

    def annual_salary(self):
        """
        计算年度薪资：乘以12得到员工年度总收入。
        :return: 年度薪资
        """
        return self.salary * 12

    def display_info(self):
        """
        展示员工的基本信息，包括姓名、职位、年度薪资。
        """
        print(f"员工姓名: {self.name}")
        print(f"职位: {self.position}")
        print(f"年度薪资: ${self.annual_salary():,.2f}")

    @classmethod
    def total_employees(cls):
        """
        类方法：用于获取公司当前员工总数。
        """
        return f"公司当前员工人数: {cls.employee_count}"

# 实例化两个员工
employee_1 = Employee("Alice", "Software Engineer", 8000)
employee_2 = Employee("Bob", "Data Scientist", 9000)

# 调用 display_info 方法，展示员工的详细信息
print("员工 1 信息：")
employee_1.display_info()

print("\n员工 2 信息：")
employee_2.display_info()

# 调用类方法，查看当前员工总数
print("\n", Employee.total_employees())
