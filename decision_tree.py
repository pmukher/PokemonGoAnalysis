import pca as pca  
import svm 
import data_cleaning as dc
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.model_selection import cross_val_score
from sklearn.metrics import precision_recall_fscore_support
from sklearn.tree import DecisionTreeClassifier
import utility as utility

if __name__ == '__main__':

    #data= pca.getData(pca.fileLocation)
    #target = pca.getLabel(pca.fileLocation)
    #data = pca.getPCA()
    target = dc.getLabel(pca.fileLocation)
    data = pca.getPCA()
    X_train, X_test, y_train, y_test = train_test_split(data,target,test_size=0.2, random_state=0)
    #print y_test.shape
    #clf = DecisionTreeClassifier(random_state=0)

    # print clf.score(X_test, y_test)

    clf = DecisionTreeClassifier(criterion="entropy", class_weight = "balanced", random_state=0)
    clf1 = DecisionTreeClassifier(criterion="entropy", class_weight = "balanced", random_state=0)
    clf1.fit(X_train, y_train)
    c, r = target.shape
    labels = target.as_matrix()
    labels = labels.reshape(c, )

    predicted = clf1.predict(X_test, check_input = True)
    print cross_val_score(clf, data, labels, cv=10)

    print utility.getClassificationReport(y_test, predicted)

