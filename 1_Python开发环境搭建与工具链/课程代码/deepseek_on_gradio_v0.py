from openai import OpenAI  # 导入OpenAI库
import gradio as gr  # 导入Gradio库用于创建Web界面

# 初始化OpenAI客户端，使用DeepSeek的API
client = OpenAI(api_key="sk-9306cd46f44a4a558e598b58929c007f", base_url="https://api.deepseek.com/v1")

def predict(message, history):
    try:
        # 将对话历史转换为OpenAI API所需的格式
        history_openai_format = []
        for human, ai in history:
            history_openai_format.append({"role": "user", "content": human})
            history_openai_format.append({"role": "assistant", "content": ai})
        history_openai_format.append({"role": "user", "content": message})
  
        try:
            # 调用DeepSeek API创建聊天完成
            response = client.chat.completions.create(
                model='deepseek-chat',
                messages=history_openai_format,
                temperature=1.0,
                stream=True
            )

            partial_message = ""
            for chunk in response:
                # 逐步构建并yield部分响应
                if chunk.choices[0].delta.content is not None:
                    partial_message += chunk.choices[0].delta.content
                    yield partial_message
        except Exception as api_error:
            # 处理API调用过程中的错误
            yield f"API Error: {str(api_error)}"
    except Exception as format_error:
        # 处理格式化历史记录时的错误
        yield f"Format Error: {str(format_error)}"

# 创建 Gradio 界面
iface = gr.ChatInterface(
    predict,
    chatbot=gr.Chatbot(height=500),
    title="DeepSeek Chat - Multi-turn Conversation",
    description="Chat with the DeepSeek AI model. Your conversation history will be maintained.",
    theme="soft",
    examples=["Hello, how are you?", "What's the weather like today?"],
)

# 启动Gradio界面
iface.launch()