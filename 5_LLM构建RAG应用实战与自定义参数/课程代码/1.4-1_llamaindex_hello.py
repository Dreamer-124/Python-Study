import os
# 设置 OpenAI API 密钥和基础URL
os.environ["OPENAI_API_KEY"] = "<your-openai-api-key>"
os.environ["OPENAI_API_BASE"] = "https://api.gpt.ge/v1"

# 将工作目录改为当前文件所在位置，确保能正确读取相对路径下的文件
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# 导入必要的LlamaIndex组件
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.embeddings.openai import OpenAIEmbedding

# 使用SimpleDirectoryReader加载指定目录下的所有文档
documents = SimpleDirectoryReader("./files").load_data()

# 配置OpenAI的embedding模型
embed_model = OpenAIEmbedding(
    model="text-embedding-3-small",  # 使用OpenAI的text-embedding-3-small模型
    api_base="https://api.gpt.ge/v1"  # 指定API基础URL
)

# 使用文档创建向量索引，并指定embedding模型
index = VectorStoreIndex.from_documents(
    documents,
    embed_model=embed_model
)

# 创建查询引擎
query_engine = index.as_query_engine()

# 执行查询并打印结果
response = query_engine.query("你是谁?")
print(response) # I am Jarvis.