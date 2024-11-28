import dashscope
from http import HTTPStatus

def embed_with_str():
    resp = dashscope.TextEmbedding.call(
        model=dashscope.TextEmbedding.Models.text_embedding_v3,
        input='衣服的质量杠杠的，很漂亮，不枉我等了这么久啊，喜欢，以后还来这里买')
    if resp.status_code == HTTPStatus.OK:
        print(resp)
    else:
        print(resp)


if __name__ == '__main__':
    embed_with_str()