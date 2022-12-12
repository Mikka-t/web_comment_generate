# -*- coding:UTF-8 -*-
from chat_downloader import ChatDownloader
from janome.tokenizer import Tokenizer

def fetch_comment(url):

    chat = ChatDownloader().get_chat(url) 
    print("fetched!")
    # こっちの方が速いのでテンプレと違います
    data=[message["message"] for message in chat]
    print("data generated")
    return data

def tokenize(url):

    data = fetch_comment(url)
    print("tokenizing...")
    t = Tokenizer()
    print("tokenizing...")
    data_comment = []
    count = 0
    for comment in data:
        if count%5000 == 0:
            print(comment)
        temp_ret = ["<start>"]

        temp_arr = [token.surface for token in t.tokenize(comment)]
        # ここで前処理を色々試す
        temp_ret.extend(temp_arr)

        temp_ret.append("<end>")
        data_comment.append(temp_ret)

        # if count % 5000 == 0:
        #     print(temp_arr)
        # ミニサイズ
        # if count == 10000:
        #     break
        count += 1

    print("tokenized!")    
    
    return data_comment

