import jieba
import logging
import document

jieba.setLogLevel(logging.INFO)


# get arguments from system terminal
# file_path_1 = sys.argv[1]
# file_path_2 = sys.argv[2]

file_path_1 = r"sim_0.8/orig.txt"
file_path_2 = r"sim_0.8/orig_0.8_mix.txt"


# read stopwords
document.read_stopwords()

# build Document object
doc_1 = document.Document(file_path_1, 1)
doc_2 = document.Document(file_path_2, 2)

# caculate similarity
cosine_similiarity = document.caculate_similarity(doc_1, doc_2)


# output
print("%f"%(cosine_similiarity))
# output_path = sys.argv[3]
# open()