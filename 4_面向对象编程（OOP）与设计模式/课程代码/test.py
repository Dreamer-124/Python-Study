from abc import ABC, abstractmethod
from typing import List

# 观察者模式
class Observer(ABC):
    @abstractmethod
    def update(self, data: str) -> None:
        pass


class Observable(ABC):
    def __init__(self):
        self._obsvers: List[Observer] = []

    def add_observer(self, observer: Observer) -> None:
        self._obsvers.append(observer)

    def remove_observer(self, observer: Observer) -> None:
        self._obsvers.remove(observer)
    
    def notify_observers(self, data: str) -> None:
        for observer in self._obsvers:
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
    # 测试观察者模式
    data_source = DataSource()
    observer = DataObserver()

    data_source.add_observer(observer)
    data_source.data = "new data"  # 输出：DataObserver received data update: new data


if __name__ == "__main__":
    main()

    