from abc import ABC, abstractmethod

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

# 测试代码
def test_strategy():
    manager = StrategyManager(KeywordSearchStrategy())
    print(manager.execute_strategy("query"))  # 输出: Keyword search results for query

    manager.set_strategy(SemanticSearchStrategy())
    print(manager.execute_strategy("query"))  # 输出: Semantic search results for query

test_strategy()