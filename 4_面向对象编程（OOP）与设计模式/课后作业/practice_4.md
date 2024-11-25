## 4. 接口与类型检查
```python
from abc import ABC, abstractmethod
from typing import List


class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount: float) -> None:
        pass


class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount: float) -> None:
        return f"Processing credit card payment of {amount}"
    

class PaypalProcessor(PaymentProcessor):
    def process_payment(self, amount: float) -> None:
        return f"Processing Paypal payment of {amount}"
    

def process_all_payment(payment_processors, amount):
    for payment_processor in payment_processors:
        print(payment_processor.process_payment(amount))


process_all_payment([CreditCardProcessor(), PaypalProcessor()], 100.0)  
```
- 程序运行截图
![程序运行截图](practice_4.png)

