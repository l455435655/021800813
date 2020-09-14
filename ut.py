import unittest
import document
import logging
import jieba

class MyClassTest(unittest.TestCase):
    def setUp(self) -> None:
        jieba.setLogLevel(logging.INFO)


    def tearDown(self) -> None:
        print("test over!")


    def test_add(self):
        print('test add')
        doc_1 = document.Document(r"sim_0.8/orig.txt")
        doc_2 = document.Document(r"sim_0.8/orig_0.8_add.txt")
        ans = document.caculate_similarity(doc_1, doc_2)
        print(ans)
        self.assertGreaterEqual(ans,0)
        self.assertLessEqual(ans,1)
    def test_del(self):
        print('test del')
        doc_1 = document.Document(r"sim_0.8/orig.txt")
        doc_2 = document.Document(r"sim_0.8/orig_0.8_del.txt")
        ans = document.caculate_similarity(doc_1, doc_2)
        print(ans)
        self.assertGreaterEqual(ans,0)
        self.assertLessEqual(ans,1)

    def test_dis_1(self):
        print('test dis_1')
        doc_1 = document.Document(r"sim_0.8/orig.txt")
        doc_2 = document.Document(r"sim_0.8/orig_0.8_dis_1.txt")
        ans = document.caculate_similarity(doc_1, doc_2)
        print(ans)
        self.assertGreaterEqual(ans,0)
        self.assertLessEqual(ans,1)

    def test_dis_3(self):
        print('test dis_3')
        doc_1 = document.Document(r"sim_0.8/orig.txt")
        doc_2 = document.Document(r"sim_0.8/orig_0.8_dis_3.txt")
        ans = document.caculate_similarity(doc_1, doc_2)
        print(ans)
        self.assertGreaterEqual(ans,0)
        self.assertLessEqual(ans,1)

    def test_dis_7(self):
        print('test dis_7')
        doc_1 = document.Document(r"sim_0.8/orig.txt")
        doc_2 = document.Document(r"sim_0.8/orig_0.8_dis_7.txt")
        ans = document.caculate_similarity(doc_1, doc_2)
        print(ans)
        self.assertGreaterEqual(ans,0)
        self.assertLessEqual(ans,1)
    def test_dis_10(self):
        print('test dis_10')
        doc_1 = document.Document(r"sim_0.8/orig.txt")
        doc_2 = document.Document(r"sim_0.8/orig_0.8_dis_10.txt")
        ans = document.caculate_similarity(doc_1, doc_2)
        print(ans)
        self.assertGreaterEqual(ans,0)
        self.assertLessEqual(ans,1)
    def test_dis_15(self):
        print('test dis_15')
        doc_1 = document.Document(r"sim_0.8/orig.txt")
        doc_2 = document.Document(r"sim_0.8/orig_0.8_dis_15.txt")
        ans = document.caculate_similarity(doc_1, doc_2)
        print(ans)
        self.assertGreaterEqual(ans,0)
        self.assertLessEqual(ans,1)
    def test_mix(self):
        print('test mix')
        doc_1 = document.Document(r"sim_0.8/orig.txt")
        doc_2 = document.Document(r"sim_0.8/orig_0.8_mix.txt")
        ans = document.caculate_similarity(doc_1, doc_2)
        print(ans)
        self.assertGreaterEqual(ans,0)
        self.assertLessEqual(ans,1)
    def test_rep(self):
        print('test rep')
        doc_1 = document.Document(r"sim_0.8/orig.txt")
        doc_2 = document.Document(r"sim_0.8/orig_0.8_rep.txt")
        ans = document.caculate_similarity(doc_1, doc_2)
        print(ans)
        self.assertGreaterEqual(ans,0)
        self.assertLessEqual(ans,1)

    def test_err_1(self):
        print('test err_1')
        self.assertRaises(FileNotFoundError, document.Document, '123')

    def test_err_2(self):
        print('test err_2')
        doc_1 = document.Document(r"1.txt")
        doc_2 = document.Document(r"2.txt")
        self.assertRaises(RuntimeError, document.caculate_similarity, doc_1, doc_2)


if __name__ == '__main__':
    unittest.main()


