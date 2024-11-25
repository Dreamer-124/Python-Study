from abc import ABC, abstractmethod
import csv
import json

class DataProcessor(ABC):
    @abstractmethod
    def process(self, data):
        """处理数据的抽象方法，子类必须实现"""
        pass

    def load_data(self, file_path):
        """加载数据的通用方法"""
        with open(file_path, 'r') as file:
            return file.read()

class CSVDataProcessor(DataProcessor):
    def process(self, data):
        """实现处理CSV数据的方法"""
        reader = csv.reader(data.splitlines())
        processed_data = [row for row in reader]
        return processed_data

class JSONDataProcessor(DataProcessor):
    def process(self, data):
        """实现处理JSON数据的方法"""
        return json.loads(data)

# 使用示例
csv_processor = CSVDataProcessor()
csv_data = csv_processor.load_data('data.csv')
processed_csv_data = csv_processor.process(csv_data)
print("Processed CSV Data:", processed_csv_data)

json_processor = JSONDataProcessor()
json_data = json_processor.load_data('data.json')
processed_json_data = json_processor.process(json_data)
print("Processed JSON Data:", processed_json_data)