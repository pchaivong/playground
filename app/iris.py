from sklearn import datasets
from sklearn import svm
from scipy.sparse import coo_matrix
from sklearn.utils import shuffle




iris = datasets.load_iris()

X = iris.data
y = iris.target


# Shuffel data a bit.
X_sparse = coo_matrix(X)
X, X_sparse, y = shuffle(X, X_sparse, y, random_state=0)

print X
print y


# Our classifier
clf = svm.SVC(probability=True)
predicts = clf.fit(X[:100], y[:100]).predict(X[100:])
prob = clf.predict_proba(X[100:])
print predicts
print prob


# Evaluate
from sklearn.metrics import accuracy_score
print "Score: %.2f " % (100* accuracy_score(y[100:], predicts, normalize=True))

print "Dumping model to file ...."
from sklearn.externals import joblib

joblib.dump(clf, '/data/iris-svm.pkl')
print "Done"
