import pandas as pd
from matplotlib import pyplot as plt
from sklearn.decomposition import *
from sklearn import preprocessing
import numpy as np
import data_cleaning as dc

#PCA fit on scaled data ?
# PCA fit_transform on scaled or unnscaled trainig set ?

fileLocation = '/home/mahendra/ALDA/Pokemon/300k.csv'
no_of_components = 28

def normalizeData(data):
    return preprocessing.scale(data)

def getRandomizedPCA (city = 'New_York'):
    global fileLocation
    global no_of_components
    data = dc.getData(fileLocation)
    data = dc.filterDataBasedOnCity(data, city)
    scaled_data = normalizeData(data)
    print '--------- Scaled Data --------------'
    print scaled_data
    print '---------- END ---------------------'
    #print data.dtypes
    #lb = preprocessing.LabelBinarizer()
    #print scaled_data
    #print lb.fit(data)
    print scaled_data.mean(axis=0)
    print scaled_data.std(axis=0)
    pca = RandomizedPCA()
    pca.fit(scaled_data)
    print pca.explained_variance_ratio_
    cumulative_variance=np.cumsum(np.round(pca.explained_variance_ratio_, decimals=4)*100)
    plt.plot(cumulative_variance)
    plt.show()
    print cumulative_variance
    pca = RandomizedPCA(n_components = no_of_components)
    return pca.fit_transform(scaled_data)


def getPCA (city = 'New_York'):
    global fileLocation
    global no_of_components
    data = dc.getData(fileLocation)
    data = dc.filterDataBasedOnCity(data, city)
    scaled_data = normalizeData(data)
    print '--------- Scaled Data --------------'
    print scaled_data
    print '---------- END ---------------------'
    #print data.dtypes
    #lb = preprocessing.LabelBinarizer()
    #print scaled_data
    #print lb.fit(data)
    print scaled_data.mean(axis=0)
    print scaled_data.std(axis=0)
    pca = PCA()
    pca.fit(scaled_data)
    print pca.explained_variance_ratio_
    cumulative_variance=np.cumsum(np.round(pca.explained_variance_ratio_, decimals=4)*100)
    plt.plot(cumulative_variance)
    plt.show()
    print cumulative_variance
    pca = PCA(n_components = no_of_components)
    return pca.fit_transform(scaled_data)

if __name__ == '__main__':
    print getPCA()
