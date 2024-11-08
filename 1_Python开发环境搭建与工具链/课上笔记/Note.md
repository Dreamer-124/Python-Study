# 任务一 Python开发环境搭建
## 1. 笔记
- 会看[python的官方文档](https://docs.python.org/zh-cn/3.10/whatsnew/3.10.html)
- 会用Anaconda进行python的依赖包管理
- 行动起来
  - 看完视频以后关掉视频，基于自己的理解再把代码敲一遍（把事情做一遍）

## 2. 命令
- 创建环境并安装openai软件包
```sh
conda create -n deepseek python=3.11 openai
```
- 激活环境
```sh
conda activate deepseek
```
- 环境变量修改
```sh
export PATH = /path/to/python:$PATH
```

# 任务二 Cursor的配置与快捷键
## 1. 笔记
- 完成安装[cursor](https://www.cursor.com/)，处理完毕配置文件，模型，提示词

## 2. 快捷键
- `CTRL/CMD + L` 打开对话框
  - 选中代码块 `CTRL/CMD + L` 根据代码块对话
- `CTRL/CMD + K` 打开生成窗口
- `CTRL/CMD + I` 打开Composer，用于多文件修改
  - 在同一窗口内完成

## 3. 注记
- @Files: 传递指定代码文件上下文
- @Code: 传递指定代码块（函数和类）上下文
- @Docs: 从官方文档获取上下文（需要先在配置文件添加文档）
- @Web: 从搜索引擎结果获取上下文
- @Folders: 传递文件目录信息上下文
- @Chat: 传递对话窗口内容上下文（仅限代码生成窗口）
- @Definitions: 传递变量和类型定义上下文（仅限代码生成窗口）
- @Git: 传递Git仓库commit历史（仅限对话窗口）
- @Codebase: 在代码仓里扫描文件传入（仅限对话窗口）

# 任务三 为Cursor更换自定义模型并实现代码注释的生成
## 1. OpenAI API文档与 key 的创建
- [OpenAI API文档](https://platform.openai.com/docs/overview)
- [API key 创建](https://platform.openai.com/api-keys)
- 需要配置文档

## 2. 国产大模型DeepSeek
- [DeepSeek API文档](https://api-docs.deepseek.com/zh-cn/)

