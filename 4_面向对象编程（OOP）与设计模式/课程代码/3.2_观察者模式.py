from abc import ABC, abstractmethod
from typing import List

# 策略模式
class Strategy(ABC):
    @abstractmethod
    def execute(self, data: str) -> str:
        pass

class KeywordSearchStrategy(Strategy):
    def execute(self, data: str) -> str:
        return f"Keyword search results for {data}"

class SemanticSearchStrategy(Strategy):
    def execute(self, data: str) -> str:
        return f"Semantic search results for {data}"

class StrategyManager:
    def __init__(self, strategy: Strategy):
        self._strategy = strategy

    def set_strategy(self, strategy: Strategy):
        self._strategy = strategy

    def execute_strategy(self, data: str) -> str:
        return self._strategy.execute(data)

# 观察者模式
class Observer(ABC):
    @abstractmethod
    def update(self, data: str) -> None:
        pass

class Observable(ABC):
    def __init__(self):
        self._observers: List[Observer] = []

    def add_observer(self, observer: Observer) -> None:
        self._observers.append(observer)

    def remove_observer(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify_observers(self, data: str) -> None:
        for observer in self._observers:
            observer.update(data)

class DataSource(Observable):
    def __init__(self):
        super().__init__()
        self._data = ""

    @property
    def data(self) -> str:
        return self._data

    @data.setter
    def data(self, value: str) -> None:
        self._data = value
        self.notify_observers(value)

class DataObserver(Observer):
    def update(self, data: str) -> None:
        print(f"DataObserver received data update: {data}")

# 测试代码
def main():
    # 测试策略模式
    manager = StrategyManager(KeywordSearchStrategy())
    print(manager.execute_strategy("query"))  # 输出: Keyword search results for query

    manager.set_strategy(SemanticSearchStrategy())
    print(manager.execute_strategy("query"))  # 输出: Semantic search results for query

    # 测试观察者模式
    data_source = DataSource()
    observer = DataObserver()

    data_source.add_observer(observer)
    data_source.data = "new data"  # 输出: DataObserver received data update: new data

if __name__ == "__main__":
    main()