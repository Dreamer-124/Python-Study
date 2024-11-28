import os
# 设置 OpenAI API 密钥和基础URL
os.environ["OPENAI_API_KEY"] = "<YOUR_API_KEY>"
os.environ["OPENAI_API_BASE"] = "https://api.gpt.ge/v1"

# 将工作目录改为当前文件所在位置，确保能正确读取相对路径下的文件
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# 导入必要的LlamaIndex组件
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.core import Settings
from llama_index.core.node_parser import SentenceSplitter

# 自定义：自定义的文本分割器
text_splitter = SentenceSplitter(
    chunk_size=1024,     # 每个块的目标大小（字符数）
    chunk_overlap=20,    # 块之间的重叠字符数
    separator=" "        # 分割文本时使用的分隔符
)

# 自定义：嵌入模型
Settings.text_splitter = text_splitter
Settings.embed_model = OpenAIEmbedding(
    model="text-embedding-3-small",
    api_base="https://api.gpt.ge/v1"
)

# 基本的 Document
from llama_index.core import Document
text_list = ["你好", "世界"]
documents = [Document(text=text) for text in text_list]
print(documents)
# [Document(id_='fd5e18cf-dbee-48c5-9dbf-98bdbbe1c989',
# ... text='你好'),
# Document(id_='74bdcb5c-edc8-4b9b-a1c6-5ba449691515', 
# ... text='世界')]

# 自定义：Document 的 metadata
metadata = {"source": "自定义"}
documents = [Document(text=text, metadata=metadata) for text in text_list]
print(documents)



# 加载文档并创建索引
documents = SimpleDirectoryReader("./files").load_data()
index = VectorStoreIndex.from_documents(documents)

# 自定义：检索，查询引擎增加相似度检索，启用流式响应
query_engine = index.as_query_engine(
    similarity_top_k=3,
    streaming=True  
)

# 执行查询并进行流式输出
response = query_engine.query("你是谁?")
# print(response) # I am Jarvis.
response.print_response_stream()  # 使用流式输出替代普通的print