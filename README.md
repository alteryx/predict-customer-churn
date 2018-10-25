# Predicting Customer Churn with a Machine Learning Scaffolding

![](images/Framework.png)

This project demonstrates applying a 3-step framework to solve problems with machine learning. The purpose of this framework
is to provide a scaffolding for rapidly developing machine learning solutions.

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

Machine learning currently is an ad-hoc process requiring a custom solution to be built for each problem. Even for the same dataset,
a slightly different prediction problem requires a solution to be built from scratch. This has made it too difficult for many companies
to take advantage of the benefits of machine learning. A standardized procedure will make it easier to solve meaningful problems
with machine learning, allowing an application of this transformative technology to a wider range of use-cases.

# Results

The notebooks document a step-by-step application of the framework to a real-world use case and dataset - predicting customer churn.
This is a critical need for subscription-based businesses and an ideal application of machine learning. 

The final results comparing several models are shown below:

| Model                                     | ROC AUC | Recall | Precision | F1 Score |
|-------------------------------------------|---------|--------|-----------|----------|
| Naive Baseline (no ml)                    | 0.5     | 3.54%  | 1.05%     | 0.0162   |
| Logistic Regression                       | 0.567   | 0.19%  | 1.13%     | 0.0032   |
| Random Forest Default                     | 0.709   | 35.9%  | 6.41%     | 0.1088   |
| Random Forest Tuned for 50% Recall        | 0.709   | 50%    | 3.63%     | 0.0677   |
| Auto-optimized Model                      | 0.709   | 0.15%  | 2.63%     | 0.0028   |
| Auto-optimized Model Tuned for 50% Recall | 0.709   | 50%    | 3.30%     | 0.0617   |

# Notebooks

1. [Partitioning Data](https://github.com/FeatureLabs/customer-churn/blob/master/churn/1.%20Partitioning%20Data.ipynb)
2. [Prediction Engineering](https://github.com/FeatureLabs/customer-churn/blob/master/churn/2.%20Prediction%20Engineering%20-%20Labeling.ipynb)
3. [Feature Engineering](https://github.com/FeatureLabs/customer-churn/blob/master/churn/3.%20Feature%20Engineering.ipynb)
4. [Feature Engineering on Spark](https://github.com/FeatureLabs/customer-churn/blob/master/churn/4.%20Feature%20Engineering%20on%20Spark.ipynb)
5. [Modeling](https://github.com/FeatureLabs/customer-churn/blob/master/churn/5.%20Modeling.ipynb)


