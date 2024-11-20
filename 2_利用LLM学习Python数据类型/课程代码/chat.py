from openai import OpenAI
import json

client = OpenAI(api_key="sk-9306cd46f44a4a558e598b58929c007f", base_url="https://api.deepseek.com")

# Round 1

messages = [{"role": "user", "content": "What's the highest mountain in the world?"}]
response = client.chat.completions.create(
    model="deepseek-chat",
    messages=messages
)

messages.append(response.choices[0].message)

# 将 response 对象及其嵌套对象转换为字典
def convert_to_dict(obj):
    if isinstance(obj, list):
        return [convert_to_dict(i) for i in obj]
    elif hasattr(obj, "__dict__"):
        obj_dict = obj.__dict__.copy()
        for key, value in obj_dict.items():
            obj_dict[key] = convert_to_dict(value)
        return obj_dict
    else:
        return obj

response_dict = convert_to_dict(response)

# 格式化输出字典
formatted_response = json.dumps(response_dict, indent=4, ensure_ascii=False)
print(formatted_response)


messages.append(response.choices[0].message)
print(f"Messages Round 1: {messages}")

# Round 2
messages.append({"role": "user", "content": "What is the second?"})
response = client.chat.completions.create(
    model="deepseek-chat",
    messages=messages
)

messages.append(response.choices[0].message)
print(f"Messages Round 2: {messages}")


# 请你实现 多轮对话功能，但是需求是
# 1 最多只保留5轮对话
# 2 每轮对话的输入和输出使用中文
