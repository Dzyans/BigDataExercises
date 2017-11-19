# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 22:28:16 2017

@author: tadah
"""
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification

X, y = make_classification(n_samples=50, n_features=4,
                            n_informative=2, n_redundant=0,
                            random_state=0, shuffle=False)

clf = RandomForestClassifier(max_depth=2, random_state=0)

clf.fit(X, y)

RandomForestClassifier(bootstrap=True, class_weight=None, criterion='gini',
            max_depth=2, max_features='auto', max_leaf_nodes=None,
            min_impurity_decrease=0.0, min_impurity_split=None,
            min_samples_leaf=1, min_samples_split=2,
            min_weight_fraction_leaf=0.0, n_estimators=10, n_jobs=1,
            oob_score=False, random_state=0, verbose=0, warm_start=False)

print(clf.feature_importances_)