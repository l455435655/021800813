from collections import defaultdict
import math
import jieba.analyse
import jieba
import re




# 停用词表
stopwords = set()
# read stopwords.txt
def read_stopwords():
    stopwords_file = open("stopwords.txt", encoding='utf-8')
    for stopword in stopwords_file.readlines():
        stopwords.add(stopword.strip())
    stopwords_file.close()





class Document:

    # 构造函数
    def __init__(self, path):
        self.__path = path
        self.__words = []
        self.__frequency_dict = defaultdict(int)


        # read txt file
        self.__file = open(path,encoding='utf-8')
        self.__text = self.__file.read()
        self.__file.close()

        # cut txt file and caculate frequency
        self.__cut_txt()
        self.__caculate_frequency()

        # sort dictionary by value
        # self.__frequency_dict = sorted(self.__frequency_dict.items(), key=lambda kv:kv[1], reverse= True)

        self.__frequency_dict = dict(self.__frequency_dict)


    # build words list
    def __cut_txt(self):

        # self.__text中去除非中文
        self.__text = re.sub(' ', '', self.__text)
        self.__text = re.sub('\n', '', self.__text)

        # 用jieba进行分词
        self.__words = jieba.lcut(self.__text)

        # 去停用词
        self.__words = [self.word for self.word in self.__words if self.word not in stopwords]
        # rebuild the text file
        self.__text = ''.join(self.__words)


    # 计算频率并生成字典
    def __caculate_frequency(self):
        for self.__word in self.__words:
            self.__frequency_dict[self.__word] += 1


    def get_text(self):
        return self.__text

    # get words list
    def get_words(self):
        return self.__words

    # 获取字典
    def get_dictionary(self):
        return self.__frequency_dict

    # get frequency
    def get_frequency(self, word)->int:
        if word in self.__frequency_dict:
            return self.__frequency_dict[word]
        else:
            return 0




# 计算余弦相似度
def caculate_similarity(doc_1:Document,doc_2:Document)->float:
    dict_1 = doc_1.get_dictionary()
    dict_2 = doc_2.get_dictionary()

    # 词袋模型
    # 手动提取频率最高的关键词
    # keywords = set()
    # keywords_num = min(20, len(dict_1), len(dict_2))
    # it_1 = iter(dict_1)
    # it_2 = iter(dict_2)
    # for i in range(keywords_num):
    #     keywords.add(next(it_1))
    #     keywords.add(next(it_2))


    # TF-IDF 模型
    # 利用 jieba 自带的 jieba.analyse 提取关键词
    keywords_num = min(len(dict_1), len(dict_2))
    keywords = set(jieba.analyse.extract_tags(doc_1.get_text(), keywords_num) + jieba.analyse.extract_tags(doc_2.get_text(), keywords_num))



    # 构造向量
    vector = []
    for keyword in keywords:
        vector.append((doc_1.get_frequency(keyword),doc_2.get_frequency(keyword)))


    # 计算余弦相似度
    v_1 = 0
    v_2 = 0
    v = 0
    for i in vector:
        v_1 += i[0]**2
        v_2 += i[1]**2
        v += (i[0] * i[1])

    cosine_similiarity = v/math.sqrt(v_1 * v_2)


    # 返回计算结果
    return cosine_similiarity

