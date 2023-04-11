# coding: utf-8
input_sentence = [['萧炎', '哥哥']]
from main import word2vec
w2v = word2vec(vocab_list=['t1', 't2'])
a, b = w2v.prepare(input_sentence)
print(a, b)