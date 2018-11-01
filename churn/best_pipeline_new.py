import numpy as np
import pandas as pd
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.feature_selection import SelectFwe, f_classif
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline, make_union
from sklearn.tree import DecisionTreeClassifier
from tpot.builtins import StackingEstimator

# NOTE: Make sure that the class is labeled 'target' in the data file
tpot_data = pd.read_csv('PATH/TO/DATA/FILE', sep='COLUMN_SEPARATOR', dtype=np.float64)
features = tpot_data.drop('target', axis=1).values
training_features, testing_features, training_target, testing_target = \
            train_test_split(features, tpot_data['target'].values, random_state=50)

# Average CV score on the training set was:0.5589461428578048
exported_pipeline = make_pipeline(
    SelectFwe(score_func=f_classif, alpha=0.045),
    StackingEstimator(estimator=DecisionTreeClassifier(criterion="gini", max_depth=10, min_samples_leaf=8, min_samples_split=16)),
    ExtraTreesClassifier(bootstrap=False, criterion="entropy", max_features=0.1, min_samples_leaf=2, min_samples_split=8, n_estimators=100)
)

exported_pipeline.fit(training_features, training_target)
results = exported_pipeline.predict(testing_features)
