class SQLQueryBuilder:
    def __init__(self, base_query):
        self.base_query = base_query

    def __call__(self, **kwargs):
        query = self.base_query
        for key, value in kwargs.items():
            placeholder = f'{{{key}}}'
            query = query.replace(placeholder, str(value))
        return query

# 创建 SQLQueryBuilder 类的实例
base_query = "SELECT * FROM users WHERE age > {age} AND city = '{city}'"
query_builder = SQLQueryBuilder(base_query)


# 像调用函数一样调用该实例来生成不同的 SQL 查询
query1 = query_builder(age=30, city='New York')
query2 = query_builder(age=25, city='San Francisco')

print(query1)  # 输出: SELECT * FROM users WHERE age > 30 AND city = 'New York'
print(query2)  # 输出: SELECT * FROM users WHERE age > 25 AND city = 'San Francisco'