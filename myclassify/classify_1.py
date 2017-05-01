import arff, numpy as np
from sklearn import linear_model
from sklearn.ensemble import RandomForestClassifier

#import data
def importData(path):
    dataset = arff.load(open(path, 'rb'))
    data = np.array(dataset['data'])
    #print data[:10]

    #extract features and labels
    features = []
    labels = []
    for d in data:
        f = []
        for i in range(len(d) - 1):
            num = float(d[i])
            if int(num) == num:
                num = int(num)
            f.append(num)
        features.append(f)

        if d[-1] == "positive":
            labels.append(1)
        else:
            labels.append(0)
    return features, labels

#import training data and test data
train_features, train_labels = importData('qa.train.arff')
test_features, test_labels = importData('qa.test.arff')

#logistic regression
logreg = linear_model.LogisticRegression()
logreg = logreg.fit(train_features, train_labels)

lab = logreg.predict(test_features)
print "============LogisticRegression labels=========="
print lab
prob = logreg.predict_proba(test_features)
print "============LogisticRegression probs=========="
print prob[:20]

#random forest
clf = RandomForestClassifier(n_estimators=150)
clf = clf.fit(train_features, train_labels)

lab = logreg.predict(test_features)
print "============RandomForest labels=========="
print lab
prob = logreg.predict_proba(test_features)
print "============RandomForest probs=========="
print prob[:20]





