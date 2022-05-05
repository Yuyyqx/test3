# 西游记词频分析
import jieba

with open('西游记.txt', "r", encoding="utf-8") as f:
    content = f.read()
    words = jieba.lcut(content)
    counts = {}
    # 同义词处理
    for word in words:
        if len(word) == 1:
            continue
        elif word == '行者' or word == '大圣' or word == '老孙':
            rword = '悟空'
        elif word == '师父' or word == '三藏' or word == '长老':
            rword = '唐僧'
        elif word == '八戒' or word == '呆子':
            rword = '八戒'
        else:
            rword = word
            counts[rword] = counts.get(rword, 0) + 1
            items = list(counts.items())
            items.sort(key=lambda x: x[1], reverse=True)
            for i in range(20):
                word, count = items[i]
                print("{0:<10}{1:>5}".format(word, count))
            f.close()

        # # 排除词处理
        # excludes = {'一个', '那里', '怎么', '我们', '不知', '两个', '什么', '不是'}
        # for word1 in excludes:
        #     del counts[word1]
        #     ls = list(counts.items())
        #     ls.sort(key=lambda x: x[1], reverse=True)
        #     for i in range(8):
        #         word1, count = ls[i]
        #         print("{0:<10}{1:>5}".format(word1, count))
