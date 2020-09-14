import math
import jieba.analyse
import jieba


class Document:

    def __init__(self, path):

        self.__path = path
        self.__words = []
        self.__tfidf = {}

        # read txt file
        try:
            self.__file = open(path, encoding='utf-8')
            self.__text = self.__file.read()
            self.__file.close()
        except:
            print("无法读取 %s"%(self.__path))
            raise

        # analyse text
        self.__analyse()


    # analyse text
    def __analyse(self):
        for word,tfidf in jieba.analyse.extract_tags(self.__text, topK=0, withWeight=True):
            self.__words.append(word)
            self.__tfidf[word] = tfidf
        # print(self.__words)

    def get_text(self) -> str:
        return self.__text

    # get words list
    def get_words(self) -> list:
        return self.__words

    # get TF-IDF
    def get_tfidf(self, word) -> float:
        return self.__tfidf.get(word, 0)



# caculate similiarity
def caculate_similarity(doc_1:Document, doc_2:Document) -> float:

    keywords_1 = set(doc_1.get_words())
    keywords_2 = set(doc_2.get_words())
    if len(keywords_1) == 0 or len(keywords_2) == 0:
        print("文本无有效词汇，请输入包含有效词汇的文本路径")
        raise

    keywords = keywords_1 and keywords_2

    # build vector
    vector = []
    for keyword in keywords:
        vector.append((doc_1.get_tfidf(keyword), doc_2.get_tfidf(keyword)))

    # caculate cosine_similiarity
    v_1 = 0
    v_2 = 0
    v = 0
    for i in vector:
        v_1 += i[0] ** 2
        v_2 += i[1] ** 2
        v += (i[0] * i[1])

    similiarity = v / math.sqrt(v_1 * v_2)


    # return caculate result
    return similiarity
