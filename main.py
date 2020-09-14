import sys
import logging
import jieba
import document


def run():
    jieba.setLogLevel(logging.INFO)

    # get arguments from system terminal
    try:
        file_path_1 = sys.argv[1]
        file_path_2 = sys.argv[2]
        output_path = sys.argv[3]
    except:
        print("缺少参数!")
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

    print("%.2f"%(cosine_similiarity))
    print("OK")


if __name__ == '__main__':
    run()