import pickle
import os
from sklearn import metrics 

def saveModel(model, filename):
   pickle.dump(model, open(filename, 'wb'))


def retrieveModel(filename):
   if os.path.isfile(filename):
     print "Loading model from %s" % filename
     return pickle.load(open(filename, 'rb'))
   else:
     print "%s : No such file found" % filename


def getClassificationReport(y_actual, y_predicted ):
  #Returns precision, recall, fscore and support for the given model
  print "RMS Error"
  print metrics.mean_squared_error(y_actual, y_predicted)**(0.5)
  return metrics.classification_report(y_actual, y_predicted)


