# coding: utf-8

import MeCab
 
mecab = MeCab.Tagger("-Ochasen")
sent = "かれのくるまでまつ"
print(mecab.parse(sent))