## 2. 使用 classmethod 创建工厂方法
```python
class Logger:
    @classmethod
    def log(cls, level):
        if level == 'INFO':
            return InfoLogger()
        elif level == 'DEBUG':
            return DebugLogger()
        elif level == 'ERROR':
            return ErrorLogger()
        else:
            raise ValueError('Invalid log level')
        

class InfoLogger(Logger):
    def log(self,msg):
        print(f'[INFO] {msg}')


class DebugLogger(Logger):
    def log(self,msg):
        print(f'[DEBUG] {msg}')


class ErrorLogger(Logger):
    def log(self,msg):
        print(f'[ERROR] {msg}')


# 测试代码
logger = Logger.log('INFO')
logger.log('This is an info message')  # 输出：INFO: This is an info message

logger = Logger.log('DEBUG')
logger.log('This is a debug message')  # 输出：DEBUG: This is a debug message

logger = Logger.log('ERROR')
logger.log('This is an error message')  # 输出：ERROR: This is an error message
```
- 程序运行截图
![程序运行截图](practice_2.png)