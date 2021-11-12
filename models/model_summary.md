# Model Summary

## Hyperparameters Tuning
Hyperparameters to be tuned for each model.

| Models                   | Hyperparameters                     | Values                                 |
| ------------------------ | ----------------------------------- | -------------------------------------- |
| DummyClassifier          | random_state                        | 0                                      |
|                          | strategy                            | stratified, most_frequent, prior, uniform |
| LogisticRegression       | random_state                        | 0                                      |
|                          | C                                   | 0.1, 1, 10                             |
|                          | solver                              | lbfgs, liblinear                       |
|                          | n_jobs                              | -1                                     |
|                          | class_weight                        | balanced                               |
| KNeighborsClassifier     | n_neighbors                         | 5, 11, 21, 41                          ||                          | weights                             | uniform, distance                      |
|                          | p                                   | 1, 2                                   |
|                          | n_jobs                              | -1                                     |
| SVC                      | C                                   | 0.1, 1, 10                             |
|                          | kernel                              | linear, poly, rbf, sigmoid             |
|                          | degree                              | 2, 3, 4                                |
|                          | gamma                               | scale, auto                            |
|                          | class_weight                        | balanced                               |
| DecisionTreeClassifier   | criterion                           | gini, entropy                          |
|                          | splitter                            | best, random                           |
|                          | max_depth                           | 3, 5, 7, 9                             |
|                          | random_state                        | 0                                      |
|                          | class_weight                        | balanced                               |
| RandomForestClassifier   | n_estimators                        | 50, 100, 200                           |
|                          | criterion                           | gini, entropy                          |
|                          | max_depth                           | 3, 5, 7, 9                             |
|                          | n_jobs                              | -1                                     |
|                          | random_state                        | 0                                      |
|                          | class_weight                        | balanced, balanced_subsample           |

## Best Hyperparameters of Each Model
Best hyperparameters of each model based on validation recall. Details of hyperparameters tuning can be found on [Weights & Biases dashboard](https://wandb.ai/titus-chin/telco-customer-churn-prediction/reports/Telco-Customer-Churn-Prediction--VmlldzoxMjE2NzE1).

| Models                   | Best Hyperparameters                | Validation Recall                      |
| ------------------------ | ----------------------------------- | -------------------------------------- |
| DummyClassifier          | random_state = 0                    | 50.23%                                 |
|                          | strategy = uniform                  |                                        |
| LogisticRegression       | random_state = 0                    | 79.55%                                 |
|                          | C = 0.1                             |                                        |
|                          | solver = lbfgs                      |                                        |
|                          | n_jobs = -1                         |                                        |
|                          | class_weight = balanced             |                                        |
| KNeighborsClassifier     | n_neighbors = 41                    | 59.03%                                 |
|                          | weights = uniform                   |                                        |
|                          | p = 1                               |                                        |
|                          | n_jobs = -1                         |                                        |
| SVC                      | C = 0.1                             | 83.61%                                 |
|                          | kernel = linear                     |                                        |
|                          | class_weight = balanced             |                                        |
| DecisionTreeClassifier   | criterion = gini                    | 79.28%                                 |
|                          | splitter = random                   |                                        |
|                          | max_depth = 5                       |                                        |
|                          | random_state = 0                    |                                        |
|                          | class_weight = balanced             |                                        |
| RandomForestClassifier   | n_estimators = 200                  | 81.55%                                 |
|                          | criterion = entropy                 |                                        |
|                          | max_depth = 3                       |                                        |
|                          | n_jobs = -1                         |                                        |
|                          | random_state = 0                    |                                        |
|                          | class_weight = balanced             |                                        |

## Performance of Each Model
Train each model with its best hyperparameters, and get its training and testing recall.

| Models                   | Training Recall                     | Testing Recall                         |
| ------------------------ | ----------------------------------- | -------------------------------------- |
| DummyClassifier          | 51.17%                              | 48.64%                                 |
| LogisticRegression       | 79.81%                              | 78.26%                                 |
| KNeighborsClassifier     | 59.96%                              | 58.70%                                 |
| SVC                      | 83.61%                              | 81.79%                                 |
| DecisionTreeClassifier   | 82.48%                              | 76.63%                                 |
| RandomForestClassifier   | 81.68%                              | 80.16%                                 |

## Best Performing Model
SVC is the best performing model because it has the highest testing recall - 81.79%.