# -*- coding: utf-8 -*-
"""
Created on Fri Jan 05 21:49:45 2018

@author: npc
"""

from gensim.models import Word2Vec   
import logging  
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from sklearn.model_selection import train_test_split
c = []

svd_test_userid = []
svd_test_pretections = []
d = []
e = []

for line in open('KNN_algopredicions_10.txt'):
    line = line.strip()
    line = line.split(':')
    svd_test_userid.append(line[0])
    svd_test_pretections.append(line[1])
for line in svd_test_pretections:
    list_ = eval(line)
    d.append(list_)
    
def load_sequence(from_path):
    with open(from_path) as fp:
        [c.append(line.strip().split(",")) for line in fp]
        
def main():
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)  
    load_sequence('comitem_user.txt') # 加载语料  
    c_train,c_text = train_test_split(c,test_size=0.2)
    model = Word2Vec(c_train, sg=1,size=40, window=3, min_count=1, workers=1, iter=400, sample=1e-4, negative=15)  # 训练skip-gram模型; 默认window=5  
    test_size = 0
    hit = 0.0
    for current_pattern in c_text:
        if current_pattern[0] in svd_test_userid:
            test_size += 1.0
            n = svd_test_userid.index(current_pattern[0])
            # Reduce the current pattern in the test set by removing the last item
            last_item = current_pattern.pop()

            # Keep those items in the reduced current pattern, which are also in the models vocabulary
            items = [it for it in current_pattern if it in model.wv.vocab]
            if len(items) <= 2:
                test_size -= 1.0
                continue

            # Predict the most similar items to items
            prediction = model.most_similar(positive=items)
            for predicted_item, score in prediction:
                e.append(predicted_item)
            finall_prediction =  list(set(e).union(set(d[n])))

            # Check if the item that we have removed from the test, last_item, is among
            # the predicted ones.
            for predict_item in finall_prediction:
                if predict_item == last_item:
                    hit += 1.0
    print 'Accuracy like measure: {}'.format(hit / test_size)

if __name__ == "__main__":  
    main()
    
