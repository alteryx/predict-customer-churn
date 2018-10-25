# A Machine Learning Framework with an Application to Predicting Customer Churn

![](images/Framework.png)

This project demonstrates applying a 3-step framework to solve problems with machine learning. The purpose of this framework
is to provide a standard scaffolding for rapidly developing machine learning solutions across industries and datasets.

# Framework Steps

1. __Prediction engineering__
  * State business need
  * Translate business requirement into machine learning task
  * Develop set of labels along with cutoff times for supervised machine learning prediction problem
2. __Feature Engineering__
  * Create features - predictor variables - out of raw data 
  * Use cutoff times to make valid features for each label
  * Apply automated feature engineering to automatically make hundreds of relevant, valid features 
3. __Modeling__
  * Train a machine learning model to predict labels from features
  * Use a pre-built solution with common libraries
  * Optimize model in line with business objectives

Machine learning currently is an ad-hoc process requiring a custom solution for each problem. Even for the same dataset,
a slightly different prediction problem requires an entire pipeline built from scratch. This has made it too difficult for many 
companies to take advantage of the benefits of machine learning. The standardized procedure presented here will make it easier to solve 
meaningful problemswith machine learning, allowing more companies to harness this transformative technology.

# Application to Customer Churn

The notebooks in this repository document a step-by-step application of the framework to a real-world use case and dataset - predicting
customer churn. This is a critical need for subscription-based businesses and an ideal application of machine learning. 

The dataset is provided by KKBOX, Asia's largest music streaming service, and can be downloaded [here](https://www.kaggle.com/c/kkbox-churn-prediction-challenge/data).

Within the overall scaffolding, several standard data science toolboxes are used to solve the problem:

* [Featuretools](https://docs.featuretools.com/#): automated feature engineering
* [Pandas](https://pandas.pydata.org): data munging and engineering
* [Scikit-Learn](http://scikit-learn.org/stable/documentation.html): standard machine learning algorithms
* [Apache Spark](https://spark.apache.org/documentation.html) with [PySpark](https://spark.apache.org/docs/latest/api/python/index.html): Running comptutations in parallel
* [TPOT (Tree-based Pipeline Optimization Tool)](https://github.com/EpistasisLab/tpot): model optimization using genetic algorithms

# Results

The final results comparing several models are shown below:

| Model                                     | ROC AUC | Recall | Precision | F1 Score |
|-------------------------------------------|---------|--------|-----------|----------|
| Naive Baseline (no ml)                    | 0.5     | 3.54%  | 1.05%     | 0.0162   |
| Logistic Regression                       | 0.567   | 0.19%  | 1.13%     | 0.0032   |
| Random Forest Default                     | 0.709   | 35.9%  | 6.41%     | 0.1088   |
| Random Forest Tuned for 50% Recall        | 0.709   | 50%    | 3.63%     | 0.0677   |
| Auto-optimized Model                      | 0.709   | 0.15%  | 2.63%     | 0.0028   |
| Auto-optimized Model Tuned for 50% Recall | 0.709   | 50%    | 3.30%     | 0.0617   |

__Final Confusion Matrix__

![](images/confusion_matrix_rf.png)

__Feature Importances__

![](images/most_important_rf.png)

# Feature Engineering with Spark

To scale the feature engineering to a large dataset, the data was partitioned and automated feature engineering was run in parallel
using Apache Spark with PySpark. 

![](images/spark-logo-trademark.png)

Featuretools supports scaling to multiple cores on one machine natively or to multiple machines using a Dask cluster. However, this
approach shows that Spark can also be used to parallelize feature engineering resulting in reduced run times even on large datasets.

![](images/featuretools-logo.png)

The notebook [Feature Engineering on Spark](https://github.com/FeatureLabs/customer-churn/blob/master/churn/4.%20Feature%20Engineering%20on%20Spark.ipynb) demonstrates the procedure. The article [Featuretools on Spark](https://medium.com/feature-labs-engineering/featuretools-on-spark-e5aa67eaf807) documents the approach.

# Notebooks

1. [Partitioning Data](https://github.com/FeatureLabs/customer-churn/blob/master/churn/1.%20Partitioning%20Data.ipynb)
2. [Prediction Engineering](https://github.com/FeatureLabs/customer-churn/blob/master/churn/2.%20Prediction%20Engineering%20-%20Labeling.ipynb)
3. [Feature Engineering](https://github.com/FeatureLabs/customer-churn/blob/master/churn/3.%20Feature%20Engineering.ipynb)
4. [Feature Engineering on Spark](https://github.com/FeatureLabs/customer-churn/blob/master/churn/4.%20Feature%20Engineering%20on%20Spark.ipynb)
5. [Modeling](https://github.com/FeatureLabs/customer-churn/blob/master/churn/5.%20Modeling.ipynb)

## Feature Labs

<p align="left">
  <img src="images/FeatureLabs.png" width = "400" alt = "Feature Labs"/>
</p>

Featuretools was created by the developers at [Feature Labs](https://www.featurelabs.com/). If building impactful data science pipelines is important to you or your business, please [get in touch](https://www.featurelabs.com/contact.html).

### Contact

Any questions can be directed to will.koehrsen@featurelabs.com
