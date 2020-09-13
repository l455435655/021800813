import sys
import jieba
import logging
import document


def run():
    jieba.setLogLevel(logging.INFO)

    # file_path_1 = r"sim_0.8/orig.txt"
    # file_path_2 = r"sim_0.8/orig_0.8_dis_10.txt"
    # output_path = r"output.txt"

    # get arguments from system terminal
    try:
        file_path_1 = sys.argv[1]
        file_path_2 = sys.argv[2]
        output_path = sys.argv[3]
    except:
        print("缺少参数!")
        return

    # read stopwords
    try:
        document.read_stopwords()
    except:
        print("无法打开 stopwords.txt")
        return

    # build Document object
    try:
        doc_1 = document.Document(file_path_1)
        doc_2 = document.Document(file_path_2)
    except:
        return

    # caculate similarity
    try:
        cosine_similiarity = document.caculate_similarity(doc_1, doc_2)
    except:
        return

    # output
    try:
        output_file = open(output_path, "w")
        output_file.write("%.2f"%(cosine_similiarity))
        output_file.close()
    except:
        print("%s打开失败 "%(sys.argv[3]))
        return

    print("OK")



if __name__ == '__main__':
    run()