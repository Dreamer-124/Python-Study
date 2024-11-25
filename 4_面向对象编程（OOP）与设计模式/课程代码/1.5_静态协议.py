from abc import ABC, abstractmethod
import csv
import json
from typing import List, Any

class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: str) -> Any:
        """处理数据的抽象方法，子类必须实现"""
        pass

    def load_data(self, file_path: str) -> str:
        """加载数据的通用方法"""
        with open(file_path, 'r') as file:
            return file.read()

class CSVDataProcessor(DataProcessor):
    def process(self, data: str) -> List[List[str]]:
        """实现处理CSV数据的方法"""
        reader = csv.reader(data.splitlines())
        processed_data = [row for row in reader]
        return processed_data

class JSONDataProcessor(DataProcessor):
    def process(self, data: str) -> Any:
        """实现处理JSON数据的方法"""
        return json.loads(data)