from openai import OpenAI  
import gradio as gr  

# 初始化OpenAI客户端
client = OpenAI(api_key="sk-eff45a3737fd4a7c9872d5388de32ea0", base_url="https://api.deepseek.com/v1")

def predict(message, history):
    try:
        history_openai_format = []
        # 将历史对话转换为OpenAI格式
        for human, ai in history:
            history_openai_format.append({"role": "user", "content": human})
            history_openai_format.append({"role": "assistant", "content": ai})
        history_openai_format.append({"role": "user", "content": message})
        # 调试
        print(history_openai_format)
        
        try:
            # 调用OpenAI的聊天完成API
            response = client.chat.completions.create(
                model='deepseek-chat',
                messages=history_openai_format,
                temperature=1.0,
                stream=True
            )

            partial_message = ""
            for chunk in response:
                if chunk.choices[0].delta.content is not None:
                    partial_message += chunk.choices[0].delta.content
                    yield partial_message
        except Exception as api_error:
            yield f"API错误: {str(api_error)}"
    except Exception as format_error:
        yield f"格式错误: {str(format_error)}"

# 创建Gradio界面
iface = gr.ChatInterface(
    predict,
    chatbot=gr.Chatbot(height=500),
    title="DeepSeek Chat - 多轮对话",
    description="与DeepSeek AI模型聊天。您的对话历史将被保留。",
    theme="soft",
    examples=["你好，你好吗？", "今天天气怎么样？"],
    css=".gradio-container .chatbot { width: 400px; }"
)

# 启动界面
iface.launch()