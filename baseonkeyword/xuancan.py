# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 20:53:29 2017

@author: npc
"""

from gensim.models import Word2Vec    
import sys
import imp
imp.reload(sys)
sys.setdefaultencoding('utf8')
from sklearn.model_selection import train_test_split
c = []

def load_sequence(from_path):
    with open(from_path) as fp:
        [c.append(line.strip().split(" ")) for line in fp]
        
def main():
    load_sequence('E:\\pythonwork\\1105\\c.txt') # 加载语料  
    c_train,c_text = train_test_split(c,test_size=0.2)
    for i in range(5,100,5):
        model = Word2Vec(c_train, size=10, window=i, min_count=1, workers=1, iter=3, sample=1e-4, negative=20)  # 训练skip-gram模型; 默认window=5  
        test_size = float(len(c_text))
        hit = 0.0
        for current_pattern in c_text:
            if len(current_pattern) < 2:
                test_size -= 1.0
                continue
            # Reduce the current pattern in the test set by removing the last item
            last_item = current_pattern.pop()

            # Keep those items in the reduced current pattern, which are also in the models vocabulary
            items = [it for it in current_pattern if it in model.wv.vocab]
            if len(items) <= 2:
                test_size -= 1.0
                continue

            # Predict the most similar items to items
            prediction = model.most_similar(positive=items)

            # Check if the item that we have removed from the test, last_item, is among
            # the predicted ones.
            for predicted_item, score in prediction:
                if predicted_item == last_item:
                    hit += 1.0
        print('Accuracy like measure: {}'.format(hit / test_size))

if __name__ == "__main__":  
    main()