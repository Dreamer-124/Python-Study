## 1. 借助大模型掌握 OOP
### 1.1 classmethod 与 staticmethod
- 使用`classmethod`创建工厂方法是一个常见的设计模式，特别是在需要根据不同的条件创建类的实例时，工厂方法可以让我们在不直接调用类构造函数的情况下创建对象
```python
class Pizza:
    def __init__(self, size, toppings):
        self.size = size
        self.toppings = toppings
    
    @classmethod
    def margherita(cls):
        return cls(size = 'Medium', toppings = ['Tomato', 'Mozzarella', 'Basil'])

    @classmethod
    def pepperoni(cls):
        return cls(size = 'Large', toppings = ['Tomato', 'Mozzarella', 'Pepperoni'])
    
    @classmethod
    def custom(cls, size, toppings):
        return cls(size, toppings)
    
    def __str__(self):
        return f"Pizza(size='{self.size}', toppings={self.toppings})"
    
# 使用工厂方法创建不同类型的Pizza
marghertia_pizza = Pizza.margherita()
pepperoni_pizza = Pizza.pepperoni()
custom_pizza = Pizza.custom('Small', ['Tomato', 'Mozzarella', 'Muchrooms'])

print(marghertia_pizza)
print(pepperoni_pizza)
print(custom_pizza)
```
- 不使用`classmethod`，直接调用类的构造函数
```python
class Pizza:
    def __init__(self, size, toppings):
        self.size = size
        self.toppings = toppings
    
    def __str__(self):
        return f"Pizza(size={self.size}, toppings={self.toppings})"
    
# 直接调用构造函数创建不同类型的Pizza
margherita_pizza = Pizza(size="Medium", toppings=["Tomato", "Mozzarella", "Basil"])
pepperoni_pizza = Pizza(size="Large", toppings=["Tomato", "Mozzarella", "Pepperoni"])
custom_pizza = Pizza(size="Small", toppings=["Tomato", "Mozzarella", "Mushrooms"])

print(margherita_pizza)
print(pepperoni_pizza)
print(custom_pizza)
```
- `staticmethod`的作用是定义一个与类相关但不依赖于类或实例的状态的方法。它通常用于封装一些逻辑，这些逻辑在概念上属于类，但是不需要访问类或实例的属性和方法。也就是说当我们需要定义一个不被类外部调用但类内部需要调用的方法时，可以使用`staticmethod`实现
```python
from typing import Any


class MathUtils:
    def __init__(self, x: Any, y: Any):
        self.x = x
        self.y = y

    @staticmethod
    def add(x, y):
        """返回两个数的和"""
        return x + y

    @staticmethod
    def subtract(x, y):
        """返回两个数的差"""
        return x - y

    @staticmethod
    def multiply(x, y):
        """返回两个数的乘积"""
        return x * y

    @staticmethod
    def divide(x, y):
        """返回两个数的商"""
        if y == 0:
            raise ValueError("除数不能为0")
        return x / y
    
    def get_result(self):
        print(f"Addition: {MathUtils.add(self.x, self.y)}")
        print(f"Subtraction: {self.subtract(self.x, self.y)}")
        print(f"Multiplication: {self.multiply(self.x, self.y)}")
        print(f"Division: {self.divide(self.x, self.y)}")
        return self.x + self.y


# 使用静态方法
result_add = MathUtils.add(10, 5)
result_subtract = MathUtils.subtract(10, 5)
result_multiply = MathUtils.multiply(10, 5)
result_divide = MathUtils.divide(10, 5)

print(f"Addition: {result_add}")
print(f"Subtraction: {result_subtract}")
print(f"Multiplication: {result_multiply}")
print(f"Division: {result_divide}")

# 使用实例方法
math_utils = MathUtils(10, 5)
result = math_utils.get_result()
print(f"Result: {result}")
```

### 1.2 私有属性与名称改写
- 实例属性`__dict__`是一个字典对象，它包含了实例的所有可变属性，通过访问__dict__，我们可以查看和修改实例的属性
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
# 创建实例
person = Person('张三', 18)

# 访问实例属性 __dict__
print(person.__dict__)  # {'name': '张三', 'age': 18}

# 修改实例属性
person.__dict__['name'] = '李四'
print(person.__dict__)  # {'name': '李四', 'age': 18}

# 添加实例属性
person.__dict__['address'] = '北京'
print(person.address)  # {'name': '李四', 'age': 18, 'address': '北京'}
```
- 定义私有属性：`__private_attribute`是一个私有属性，通过在属性名前加双下划线定义
- 私有属性的名称在`__dict__`中被改写为`_MyClass__private_attribute`
- 名称改写是一种安全措施，不能保证万无一失：它的目的是避免意外访问，不能防止故意做错事
```python
class Person:
    def __init__(self, name, age):
        self.__name = name  # 私有属性
        self.__age = age    # 私有属性

    # 公共方法，用于获取私有属性__name
    def get_name(self):
        return self.__name

    # 公共方法，用于获取私有属性__age
    def get_age(self):
        return self.__age

    # 公共方法，用于设置私有属性__age
    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("年龄必须大于0")

# 创建Person类的实例
person = Person("Alice", 30)

# 直接访问私有属性（不推荐，违反了封装原则）
# print(person.__name)  # 这将引发错误，因为__name是私有的
# print(person.__age)   # 这将引发错误，因为__age是私有的

# 使用公共方法访问私有属性
print(person.get_name())  # 输出: Alice
print(person.get_age())   # 输出: 30

# 使用公共方法设置私有属性
person.set_age(35)
print(person.get_age())   # 输出: 35

# 尝试设置无效的年龄
person.set_age(-5)        # 输出: 年龄必须大于0
print(person.get_age())   # 输出: 35，年龄没有改变
```

### 1.3 猴子补丁
- 猴子补丁是一种在运行时动态修改模块、类或函数的方法，用于增强功能或修复缺陷，例如，网络库`gevent`对部分`Python`标准库进行了猴子补丁，以实现一种轻量级并发模型，而无需依赖线程或`async/await`
- 猴子补丁应谨慎使用，因为它可能导致代码难以维护和调试
- 当我们在调用原始的库并且没有办法对原始库进行修改的前提，然后由我们自己来维护的代码，可以使用猴子补丁
```python
import time

class Myclass:
    def original_method(self):
        return "这是原始方法"
    
# 定义一个新方法，用于替换原始方法
def patch_method(self):
    print("开始执行新方法")
    start_time = time.time()

    # 调用原始方法
    original_result = original_method_backup(self)

    end_time = time.time()
    print("新方法执行完")
    print(f"执行时间: {end_time - start_time} 秒")

    return original_result

# 备份原始方法
original_method_backup = Myclass.original_method

# 使用猴子补丁替换原始方法
Myclass.original_method = patch_method

# 创建实例并调用被补丁的方法
instance = Myclass()
print(instance.original_method())
```

### 1.4 接口与类型检查
- 在`Python`中没有`interface`关键字，我们使用抽象基类（ABC）来定义接口，并在运行时显式检查类型（静态类型检查工具也支持）
- 抽象基类补充了鸭子类型，提供了一种定义接口的方式
```python
from abc import ABC, abstractmethod
import csv
import json

class DataProcessor(ABC):
    @abstractmethod
    def process(self, data):
        """处理数据的抽象方法，子类必须实现"""
        pass

    @abstractmethod
    def load_data(self, file_path):
        """加载数据的通用方法"""
        with open(file_path, 'r') as file:
            return file.read()
        
class CSVDataProcessor(DataProcessor):
    def process(self, data):
        """实现处理CSV数据的方法"""
        reader = csv.reader(data.splitlines())
        process_data = [row for row in reader]
        return process_data

class JSONDataProcessor(DataProcessor):
    def process(self, data):
        """实现处理JSON数据的方法"""
        return json.loads(data)
    
# 使用示例
csv_processor = CSVDataProcessor()
csv_data = csv_processor.load_data('data.csv')
processed_csv_data = csv_processor.process(csv_data)
print(f"processed_csv_data: {processed_csv_data}")

json_processor = JSONDataProcessor()
json_data = json_processor.load_data('data.json')
processed_json_data = json_processor.process(json_data)
print(f"processed_json_data: {processed_json_data}")
```

### 1.5 静态协议与类型注解
- 类型注解：显式标明数据类型，提高代码可读性和静态分析能力，有助于大型项目的代码维护
```python
import csv
import json

from abc import ABC, abstractmethod
from typing import Any, List

class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: str) -> Any:
        """处理数据的抽象方法，子类必须实现"""
        pass

    @abstractmethod
    def load_data(self, file_path: str) -> str:
        """加载数据的通用方法"""
        with open(file_path, 'r') as file:
            return file.read()
        
class CSVDataProcessor(DataProcessor):
    def process(self, data: str) -> List[List[str]]:
        """实现处理CSV数据的方法"""
        reader = csv.reader(data.splitlines())
        process_data = [row for row in reader]
        return process_data

class JSONDataProcessor(DataProcessor):
    def process(self, data: str) -> Any:
        """实现处理JSON数据的方法"""
        return json.loads(data)
```

## 2. 继承
### 2.1 super()函数
- 在面向对象编程中，`super()`函数用于调用父类的方法
- `super.__init__`和`super.__setitem__`是两种常见的使用方式，分别用于调用父类的构造函数和父类的`__setitem__`方法
```python
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"Nmae: {self.name}, Age: {self.age}"
    
class Employee(Person):
    def __init__(self, name: str, age: int, position: str, salary: float):
        super().__init__(name, age)  # 调用父类的构造函数
        self.position = position
        self.salary = salary
    
    def __str__(self):
        return f"{super().__str__()}, Position: {self.position}, Salary: {self.salary}"
    

# 测试代码
employee = Employee('Tom', 25, 'Software Engineer', 3000)
print(employee)  # Name: Tom, Age: 25, Position: Software Engineer, Salary: 3000.0
```
- 有一个自定义的字典类`loggingDict`，它在每次设置键值对时记录日志，我们希望创建一个子类`ValidateDict`，它在记录日志的同时，还对键值对进行验证
- 注意：内置类型的子类覆盖的方法可能不会隐式调用，例如，`dict`的子类覆盖的`__getitem__()`方法不会被内置类型的`get()`方法调用
```python
from collections import UserDict

class LoggingDict(UserDict):
    def __setitem__(self, key, value):
        print(f"Setting {key} to {value}")
        super().__setitem__(key, value)  # 调用父类的 __setitem__ 方法

class ValidateDict(LoggingDict):
    def __setitem__(self, key, value):
        if not isinstance(key, str):
            raise TypeError(f"Key must be a string")
        if not isinstance(value, int):
            raise TypeError(f"Value must be an integer")
        super().__setitem__(key, value)  # 调用父类的 __setitem__ 方法

# 测试代码
validate_dict = ValidateDict()
validate_dict['age'] = 30  # 输出: Setting age to 30
print(validate_dict)  # 输出: {'age': 30}

# 尝试设置无效的键值对
try:
    validate_dict[10] = "thirty"
except TypeError as e:
    print(e)  # 输出: Key must be a string
```

### 2.2 混入Mixin
- 混入类 (Mixin) 是一种设计模式，用于在不使用多重继承的情况下向类添加功能，`Mixin`类通常不独立存在，而是与其他类组合使用，以增强功能或添加行为
- `Mixin`类的特点
 - 单一职责：`Mixin`类通常只提供一种特定的功能，不涉及类的核心业务逻辑
 - 组合使用：`Mixin`类通过多继承与其他类组合使用，以增强功能
 - 不独立实例化：`Mixin`类通常不独立实例化，而是作为其他类的基类
- 有一个基本的`DataProcessor`类，我们希望通过`Mixin`类为其添加数据验证和日志记录功能
```python
from abc import ABC, abstractmethod

class ValidatorMixin:
    def validate(self, data: dict) -> bool:
        for key, value in data.items():
            if not isinstance(key, str) or not isinstance(value, (int, float)):
                return False
        return True
    
class LoggerMixin:
    def log(self, message: str) -> None:
        print(f"[LOG]: {message}")

class DataProcesser(ABC):
    @abstractmethod
    def process(self, data: dict) -> None:
        """处理数据的抽象方法，子类必须实现"""
        raise NotImplementedError("Subclasses should implement this method")
    
class ValidatedLoggedDataProcessor(DataProcesser, ValidatorMixin, LoggerMixin):
    def process(self, data: dict) -> None:
        if not self.validate(data):
            self.log("Invalid data")
            return
        self.log("Processing data")
        # 处理数据逻辑
        print("Data processed:", data)


# 测试代码
processor = ValidatedLoggedDataProcessor()
data = {"temperature": 26.5, "humidity": 65}
processor.process(data)  # 输出: Validation succeeded           

invalid_data = {123: "invalid"}
processor.process(invalid_data)  # 输出: Validation failed
```


## 3. 设计模式与代码复用的提升
### 3.1 SOLID 原则的实践
- 单一职责原则(SRP)：拆分大型类，使每个类只负责一项功能
```python
class Report:
    def __init__(self, content):
        self.content = content

class FileManager:
    @staticmethod
    def save_to_file(report, filename):
        with open(filename, 'w') as f:
            f.write(report.content)

class ReportPrinter:
    @staticmethod
    def print_report(report):
        print(report.content)

# Report 类只负责保存内容，其他职责由各自的类负责
```
- 开闭原则(OCP)：通过接口和抽象类，支持系统的扩展而无需修改已有代码
```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        print("Drawing a circle")

class Rectangle(Shape):
    def draw(self):
        print("Drawing a rectangle")

class GraphicEditor:
    def draw_shape(self, shape: Shape):
        shape.draw()

# 新增形状时，只需实现 draw 方法，不改动 GraphicEditor
```
- 里氏替换原则(LSP)：确保子类能够替换父类而不改变系统行为
```python
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

# Rectangle 和 Square 彻底解耦，实现 LSP
```
- 接口隔离原则(ISP)：为不同的客户端提供专用接口，避免冗余
```python
class Workable(ABC):
    @abstractmethod
    def work(self):
        pass

class Eatable(ABC):
    @abstractmethod
    def eat(self):
        pass

class Worker(Workable, Eatable):
    def work(self):
        print("I'm working.")

    def eat(self):
        print("I'm eating.")

class Robot(Workable):
    def work(self):
        print("I'm working.")
```
- 依赖倒置原则(DIP)：高层模块不依赖于低层模块，二者都依赖于抽象
```python
class Switchable(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

class LightBulb(Switchable):
    def turn_on(self):
        print("LightBulb: Bulb turned on")

    def turn_off(self):
        print("LightBulb: Bulb turned off")

class Switch:
    def __init__(self, device: Switchable):
        self.device = device

    def operate(self, on):
        if on:
            self.device.turn_on()
        else:
            self.device.turn_off()

Switch(LightBulb()).operate(True)  # 使用起来只需要更换 LightBulb 类，更加方便
```

### 3.2 设计模式
- 设计模式的三大基本分类：创建型模式、结构型模式、行为型模式
- 创建型模式：工厂模式的深入应用
 - 背景：在大型语言模型（LLM）系统中，不同的任务可能需要不同的模型组件，如预处理器、嵌入器等。为了提高系统的灵活性和可扩展性，我们可以使用工厂模式来动态创建这些组件
 - 思路：
  - 定义组件接口：定义所有组件的共同接口，例如，首先定义一个通用的组件接口`Component`，所有具体组件都将实现这个接口
  ```python
    from abc import ABC, abstractmethod

    class Component(ABC):
        @abstractmethod
        def process(self, datd: str) -> str:
            pass
  ```
  - 实现具体组件：实现不同的具体组件，如文本预处理器、词向量嵌入等，例如，实现几个具体的组件，如`TextPreprocessor`和`WordEmbedder`
  ```python
    class TextPreprocessor(Component):
        def process(self, data: str) -> str:
            # 简单的文本预处理逻辑
            return data.lower().strip()


    class WordEmbedder(Component):
        def process(self, data: str) -> str:
            # 简单的词嵌入逻辑
            return f"Embedded({data})"
  ``` 
  - 创建组件工厂：实现一个工厂类，根据配置或参数动态创建组件实例
  ```python
    # 创建组件工厂
    class ComponentFactory:
        @staticmethod
        def create_component(component_type: str) -> Component:
            if component_type == "preprocessor":
                return TextPreprocessor()
            elif component_type == "embedder":
                return WordEmbedder()
            else:
                raise ValueError(f"Unknown component type: {component_type}")
  ```
  - 遵循开闭原则：确保系统对扩展开放，对修改封闭
```python
# 定义组件接口
from abc import ABC, abstractmethod

class Component(ABC):
    @abstractmethod
    def process(self, datd: str) -> str:
        pass

# 实现具体组件
class TextPreprocessor(Component):
    def process(self, data: str) -> str:
        # 简单的文本预处理逻辑
        return data.lower().strip()

class WordEmbedder(Component):
    def process(self, data: str) -> str:
        # 简单的词嵌入逻辑
        return f"Embedded({data})"
    
# 创建组件工厂
class ComponentFactory:
    @staticmethod
    def create_component(component_type: str) -> Component:
        if component_type == "preprocessor":
            return TextPreprocessor()
        elif component_type == "embedder":
            return WordEmbedder()
        else:
            raise ValueError(f"Unknown component type: {component_type}")
        
# 测试代码
def main():
    config = ["preprocessor", "embedder"]
    data = "Hello, World!"
    for component_type in config:
        component = ComponentFactory.create_component(component_type)
        processed_data = component.process(data)
        print(f"{component_type.capitalize()} output: {processed_data}")

if __name__ == "__main__":
    main()
```

- 结构型模式：装饰器模式与描述符的结合，探讨装饰器模式和描述符在增强类功能、避免重复代码方面的作用。为类或函数添加缓存、日志记录、输入验证等功能，提高代码的可复用性
 - 思路：
  - 装饰器模式：使用类装饰器为检索组件添加缓存机制，提高性能，首先定义一个类装饰器`CacheDecorator`，为检索组件添加缓存机制
  - 描述符：利用描述符实现属性的类型检查和访问控制，防止错误使用
  - 单一职责原则：每个类或函数只负责一项功能


