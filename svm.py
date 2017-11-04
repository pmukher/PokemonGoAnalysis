import data_cleaning as dc
import pca as pca
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.svm import SVC
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.model_selection import GridSearchCV
import numpy as np
import sys

def gridSearch(data, target):
    #C_range = np.logspace(-2, 10, 13)
    #gamma_range = np.logspace(-9, 3, 13)
    #LIBSVM Default parameters
    #C_range = np.logspace(-5,15,2)
    #C_range = [-5,-3,-1,1,3,5,7,9,11,13]
    #gamma_range = np.logspace(-15,3,2)
    #gamma_range = [-15, 13]
    C_range = [1, 10, 100, 1000]
    gamma_range = [1e-3, 1e-4]
    param_grid = dict(gamma=gamma_range, C=C_range)
    cv = StratifiedShuffleSplit(n_splits=2, test_size=0.2, random_state=42)
    grid = GridSearchCV(SVC(), param_grid=param_grid, cv=cv, n_jobs=3)
    grid.fit(data, target)
    print("The best parameters are %s with a score of %0.2f"
          % (grid.best_params_, grid.best_score_))
    fp = open('logfile.txt', 'a')
    fp.write("The best parameters are %s with a score of %0.2f" % (grid.best_params_, grid.best_score_))
    fp.close()

def trainAndTestModel(data, labels, train_index, test_index, c =0.5, gamma = 0.125):
    X_train, X_test, y_train, y_test = data[train_index], data[test_index], labels[train_index], labels[test_index]
    clf = SVC( kernel='rbf', C=c, gamma = gamma)
    clf.fit(X_train, y_train)
    return clf.score(X_test, y_test)


if __name__ == '__main__':

    #data= pca.getData(pca.fileLocation)
    #data = pca.normalizeData(data)
    target = dc.getLabel(pca.fileLocation)
    data = pca.getPCA()
    gridSearch(data, target)
    sys.exit(0)
    #print y_test.shape
    #clf = DecisionTreeClassifier(random_state=0)
    #clf.fit(X_train, y_train)
    # print clf.score(X_test, y_test)
    ##X_train, X_test, y_train, y_test = train_test_split(data, target, test_size=0.2, random_state=0)
    clf = SVC()
    #clf.fit(X_train, y_train)
    #print clf.score(X_test, y_test)
    labels = target.as_matrix()
    c, r = target.shape
    labels = labels.reshape(c, )
    print cross_val_score(clf,data, labels, cv=3, n_jobs = 3)

