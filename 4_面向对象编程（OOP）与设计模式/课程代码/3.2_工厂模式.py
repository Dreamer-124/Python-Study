# 定义组件接口
from abc import ABC, abstractmethod

class Component(ABC):
    @abstractmethod
    def process(self, data: str) -> str:
        pass

# 实现具体组件
class TextPreprocessor(Component):
    def process(self, data: str) -> str:
        return data.lower().strip()

class WordEmbedder(Component):
    def process(self, data: str) -> str:
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
    data = "  Hello World!  "

    for component_type in config:
        component = ComponentFactory.create_component(component_type)
        processed_data = component.process(data)
        print(f"{component_type.capitalize()} output: {processed_data}")

if __name__ == "__main__":
    main()