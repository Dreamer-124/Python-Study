from abc import ABC, abstractmethod

class ValidatorMixin:
    def validate(self, data: dict) -> bool:
        for key, value in data.items():
            if not isinstance(key, str) or not isinstance(value, (int, float)):
                return False
        return True

class LoggerMixin:
    def log(self, message: str) -> None:
        print(f"[LOG] {message}")

class DataProcessor(ABC):
    # 处理数据的抽象方法，子类必须实现
    @abstractmethod
    def process(self, data: dict) -> None:

        raise NotImplementedError("Subclasses should implement this method.")

class ValidatedLoggedDataProcessor(DataProcessor, ValidatorMixin, LoggerMixin):
    def process(self, data: dict) -> None:
        if not self.validate(data):
            self.log("Invalid data")
            return
        self.log("Processing data")
        # 处理数据的逻辑
        print("Data processed:", data)

# 测试代码
processor = ValidatedLoggedDataProcessor()
data = {"temperature": 23.5, "humidity": 60}
processor.process(data)  # 输出: [LOG] Processing data \n Data processed: {'temperature': 23.5, 'humidity': 60}

invalid_data = {123: "invalid"}
processor.process(invalid_data)  # 输出: [LOG] Invalid data