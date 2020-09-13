import unittest
import document
import logging
import jieba

class MyClassTest(unittest.TestCase):
    def setUp(self) -> None:
        jieba.setLogLevel(logging.INFO)
        self.doc_1 = document.Document(r"sim_0.8/orig.txt")
        self.doc_2 = document.Document(r"sim_0.8/orig_0.8_dis_10.txt")
        document.read_stopwords()

    def tearDown(self) -> None:
        print("test over")


    def test_caculate(self):
        ans = document.caculate_similarity(self.doc_1,self.doc_2)
        print(ans)
        self.assertGreaterEqual(ans,0)
        self.assertLessEqual(ans,1)


if __name__ == '__main__':
    unittest.main()


