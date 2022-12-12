
from nltk import ngrams
import random
from collections import Counter, defaultdict

import fetch

def generate(url):

    num = 30  # 生成するコメント数
    print("fetching",url)
    data_comment = fetch.tokenize(url)
    print("generating")

    trigram = []
    # トライグラム
    for sentence in data_comment:
        trigram.extend(list(ngrams(sentence,3)))
    count_dict = Counter(trigram)

    malkov_dict = defaultdict(lambda: {"word":[], "weight":[]})
    head_dict = defaultdict(lambda: int)
    for key, value in count_dict.items():
        word_12 = key[:2]
        word_3 = key[2]
        malkov_dict[word_12]["word"].append(word_3)
        malkov_dict[word_12]["weight"].append(value)
        # 文頭の情報
        if key[0]=="<start>":
            head_dict[key[1]] = value
    head_word = [i for i in head_dict.keys()]
    head_weight = [i for i in head_dict.values()]

    ret = ['']*num

    for i in range(num):
        head = random.choices(head_word, k=1, weights=head_weight)[0]
        ans = ["<start>",head]

        while True:
            ref = tuple(ans[-2:])
            word = malkov_dict[ref]["word"]
            weight = malkov_dict[ref]["weight"]
            next_word = random.choices(word, weights=weight, k=1)[0]
            if next_word == "<end>":
                break
            ans.append(next_word)
        ret[i] = "".join(ans[1:])
        print("generated", ret[i])
    
    return ret