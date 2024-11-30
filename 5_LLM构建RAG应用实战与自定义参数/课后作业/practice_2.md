## 2. 文件类型统计器 - 编写函数统计目录中的文件总数、总大小(MB)和各类型文件数量分布。
```python
import os


def static_dir(dir_path):
    # 统计目录中的文件总数、总大小和各类型文件数量分布
    file_count = 0
    total_size = 0
    type_count = {}
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            file_count += 1
            file_path = os.path.join(root, file)
            total_size += os.path.getsize(file_path)
            file_type = file.split(".")[-1]
            if file_type in type_count:
                type_count[file_type] += 1
            else:
                type_count[file_type] = 1

    return f"file_count: {file_count}, total_size: {total_size}, type_count: {type_count}"


# 测试代码
if __name__ == "__main__":
    dir_path = "D:/Desktop/www/Python-Study/4_面向对象编程（OOP）与设计模式/课程代码"
    print(static_dir(dir_path))
```

- 程序运行截图
![程序运行截图](practice_2.png)