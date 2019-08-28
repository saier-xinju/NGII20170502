# -*- coding: utf-8 -*-
"""
Created on Fri Jan 05 18:28:32 2018

@author: npc
"""

from collections import defaultdict  
  
from surprise import KNNWithMeans  
from surprise import Dataset  
from surprise import dataset  
  
def get_top_n(predictions, n=10):  
    '''''Return the top-N recommendation for each user from a set of predictions. 
 
    Args: 
        predictions(list of Prediction objects): The list of predictions, as 
            returned by the test method of an algorithm. 
        n(int): The number of recommendation to output for each user. Default 
            is 10. 
 
    Returns: 
    A dict where keys are user (raw) ids and values are lists of tuples: 
        [(raw item id, rating estimation), ...] of size n. 
    '''  
  
    # First map the predictions to each user.，这句默认的list类型  
    top_n = defaultdict(list)  
      
    #uid为用户id，iid为项目id，true_r为真实的概率，est为分解后的估值  
    for uid, iid, true_r, est, _ in predictions:  
        top_n[uid].append((iid, est))  
  
    # Then sort the predictions for each user and retrieve the k highest ones.  
    for uid, user_ratings in top_n.items():  
        user_ratings.sort(key=lambda x: x[1], reverse=True)  
        top_n[uid] = user_ratings[:n]  
  
    return top_n  
  
  
# 加载数据集  
  
reader=dataset.Reader(line_format='user item rating', sep='\t')  
data =Dataset.load_from_file('u.data',reader)  
trainset = data.build_full_trainset()  
algo = KNNWithMeans()  
algo.train(trainset)  
  
#推荐不在训练数据集里得Top—N个数据  
# Than predict ratings for all pairs (u, i) that are NOT in the training set.  
testset = trainset.build_anti_testset()  
predictions = algo.test(testset)  
  
top_n = get_top_n(predictions, n=10)  
w = open('KNNWithMeans_algopredicions_10.txt','w+')  
# Print the recommended items for each user  
for uid, user_ratings in top_n.items():  
    w.write(str(uid)+':'+str([iid for (iid, _) in user_ratings])+'\n')
w.close()