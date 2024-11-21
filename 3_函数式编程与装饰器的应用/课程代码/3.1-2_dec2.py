# langchain cache.py
# 定义两个装饰器 log_execution 和 measure_time。
# 在 InMemoryCache 类的方法上叠放这两个装饰器。
import time
from typing import Any, Callable, Dict, Optional, Tuple, TypeVar
from functools import wraps

RETURN_VAL_TYPE = TypeVar('RETURN_VAL_TYPE')

def log_execution(func: Callable) -> Callable:
    """Decorator to log the execution of a function."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Executing {func.__name__} with args: {args} and kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"Finished executing {func.__name__}")
        return result
    return wrapper

def measure_time(func: Callable) -> Callable:
    """Decorator to measure the execution time of a function."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds")
        return result
    return wrapper

class InMemoryCache(BaseCache):
    """Cache that stores things in memory."""

    def __init__(self) -> None:
        """Initialize with empty cache."""
        self._cache: Dict[Tuple[str, str], RETURN_VAL_TYPE] = {}

    @log_execution
    @measure_time
    def lookup(self, prompt: str, llm_string: str) -> Optional[RETURN_VAL_TYPE]:
        """Look up based on prompt and llm_string."""
        return self._cache.get((prompt, llm_string), None)

    @log_execution
    @measure_time
    def update(self, prompt: str, llm_string: str, return_val: RETURN_VAL_TYPE) -> None:
        """Update cache based on prompt and llm_string."""
        self._cache[(prompt, llm_string)] = return_val

    @log_execution
    @measure_time
    def clear(self, **kwargs: Any) -> None:
        """Clear cache."""
        self._cache = {}

    @log_execution
    @measure_time
    async def alookup(self, prompt: str, llm_string: str) -> Optional[RETURN_VAL_TYPE]:
        """Look up based on prompt and llm_string."""
        return self.lookup(prompt, llm_string)

    @log_execution
    @measure_time
    async def aupdate(
        self, prompt: str, llm_string: str, return_val: RETURN_VAL_TYPE
    ) -> None:
        """Update cache based on prompt and llm_string."""
        self.update(prompt, llm_string, return_val)

    @log_execution
    @measure_time
    async def aclear(self, **kwargs: Any) -> None:
        """Clear cache."""
        self.clear()