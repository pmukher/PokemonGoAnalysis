from sklearn.neighbors import KNeighborsClassifier
import data_cleaning as dc
import pca as pca
import numpy as np
from matplotlib import pyplot as plt
import sys
from sklearn.model_selection import cross_val_score, train_test_split
import utility as utility

def knn():
    target = dc.getLabel(pca.fileLocation)
    data = pca.getPCA()
    x = []
    y = []
    #X = [[0], [1], [2], [3]]
    #y = [0, 0, 1, 1]
    c, r = target.shape
    labels = target.as_matrix()
    labels = labels.reshape(c, )
    #neigh.fit(X,y)
    #print neigh.predict([[1.1]])
    '''
    for i in xrange(5,26,5):
        neigh = KNeighborsClassifier(n_neighbors=15, algorithm='ball_tree')
        scores = cross_val_score(neigh, data, labels, cv=i)
        x.append(i)
        y.append(max(scores))
        print '------------------------------------------------------------'
        print i
        print scores
    print '------------------------------------------------------------'
    '''
    X_train, X_test, y_train, y_test = train_test_split(data,target,test_size=0.2, random_state=0)
    neigh = KNeighborsClassifier(n_neighbors=15, algorithm='ball_tree')
    neigh1 = KNeighborsClassifier(n_neighbors=15, algorithm='ball_tree')
    neigh1.fit(X_train, y_train)
    predicted = neigh1.predict(X_test)
    print utility.getClassificationReport(y_test, predicted)
    scores = cross_val_score(neigh, data, labels, cv=10)
    #plt.plot(x,y)
    #plt.show()

def main():
    knn()

if __name__=='__main__':
    main()
