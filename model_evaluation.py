from sklearn.model_selection import KFold
import pca as pca
import data_cleaning as dc
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
import numpy as np
import svm as svm

if __name__ == '__main__':
    best_test = []
    best_train = []
    best_score = -9999
    target = dc.getLabel(pca.fileLocation)
    data = pca.getPCA()
    labels = target.as_matrix()
    c, r = target.shape
    labels = labels.reshape(c, )

    cv = KFold(n_splits=10)
    fold = 1
    for train, test in cv.split(data):
        X_train, X_test, y_train, y_test = data[train], data[test], labels[train], labels[test]
        print "Performing Decision tree validation (Fold %d )"% fold
        clf = DecisionTreeClassifier(criterion="entropy", class_weight="none", random_state=0)
        clf.fit(X_train, y_train)
        current_score = clf.score(X_test, y_test)
        print "Fold %d score %d"%(fold, current_score)
        fold = fold + 1
        if best_score < current_score :
            best_score = current_score
            best_test = np.copy(test)
            best_train = np.copy(train)


    print "Best Decision tree classifier score :", best_score
    print "Performing SVM validation :"
    svm_score = svm.trainAndTestModel(data, labels, best_train, best_test)
    print "SVM Score : ", svm_score
