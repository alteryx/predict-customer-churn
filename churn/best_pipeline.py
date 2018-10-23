import numpy as np
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import MinMaxScaler

# NOTE: Make sure that the class is labeled 'target' in the data file
tpot_data = pd.read_csv('PATH/TO/DATA/FILE', sep='COLUMN_SEPARATOR', dtype=np.float64)
features = tpot_data.drop('target', axis=1).values
training_features, testing_features, training_target, testing_target = \
            train_test_split(features, tpot_data['target'].values, random_state=None)

# Average CV score on the training set was:0.43811110082970917
exported_pipeline = make_pipeline(
    MinMaxScaler(),
    GradientBoostingClassifier(learning_rate=0.01, max_depth=7, max_features=0.7500000000000001, min_samples_leaf=12, min_samples_split=3, n_estimators=100, subsample=0.05)
)

exported_pipeline.fit(training_features, training_target)
results = exported_pipeline.predict(testing_features)
