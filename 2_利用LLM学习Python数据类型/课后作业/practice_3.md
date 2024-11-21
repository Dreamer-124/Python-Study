## 1. 实现图的常用操作
```python
class Graph:
    def __init__(self):
        """初始化一个空的图"""
        self.adjacency_list = {}

    def add_node(self, node):
        """添加节点"""
        if node not in self.adjacency_list:
            self.adjacency_list[node] = []

    def add_edge(self, node1, node2):
        """添加无向边"""
        if node1 not in self.adjacency_list:
            self.add_node(node1)
        if node2 not in self.adjacency_list:
            self.add_node(node2)
        self.adjacency_list[node1].append(node2)
        self.adjacency_list[node2].append(node1)

    def dfs(self, start_node):
        """深度优先搜索"""
        visited = set()
        result = []
        self._dfs_recursive(start_node, visited, result)
        return result

    def _dfs_recursive(self, node, visited, result):
        """递归实现DFS"""
        if node not in visited:
            visited.add(node)
            result.append(node)
            for neighbor in self.adjacency_list[node]:
                self._dfs_recursive(neighbor, visited, result)

    def bfs(self, start_node):
        """广度优先搜索"""
        visited = set()
        queue = [start_node]
        result = []

        while queue:
            node = queue.pop(0)
            if node not in visited:
                visited.add(node)
                result.append(node)
                queue.extend(
                    neighbor for neighbor in self.adjacency_list[node]
                    if neighbor not in visited
                )

        return result

# Example usage:
if __name__ == "__main__":
    graph = Graph()
    graph.add_node("A")
    graph.add_node("B")
    graph.add_node("C")
    graph.add_edge("A", "B")
    graph.add_edge("A", "C")
    graph.add_edge("B", "C")

    print("DFS starting from A:", graph.dfs("A"))  # Output: ['A', 'B', 'C']
    print("BFS starting from A:", graph.bfs("A"))  # Output: ['A', 'B', 'C']
```
- 程序运行截图如下
![图的常用操作实现截图](practice_3.png)