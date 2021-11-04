# Model Summary

## Hyperparameters Tuning
Hyperparameters to be tuned for each model.

| Models                   | Hyperparameters                     | Values                                 |
| ------------------------ | ----------------------------------- | -------------------------------------- |
| DummyClassifier          | random_state                        | 0                                      |
|                          | strategy                            | stratified, most_frequent, prior, uniform |
| LogisticRegression       | random_state                        | 0                                      |
|                          | C                                   | 0.0001, 0.001, 0.01, 0.1, 1, 10, 100   |
|                          | solver                              | newton-cg, lbfgs, liblinear, sag, saga |
|                          | n_jobs                              | -1                                     |
| KNeighborsClassifier     | n_neighbors                         | 5, 11, 21, 41, 81, 161, 321            ||                          | weights                             | uniform, distance                      |
|                          | algorithm                           | auto, ball_tree, kd_tree, brute        |
|                          | p                                   | 1, 2                                   |
|                          | n_jobs                              | -1                                     |
| SVC                      | C                                   | 0.0001, 0.001, 0.01, 0.1, 1, 10, 100   |
|                          | kernel                              | linear, poly, rbf, sigmoid             |
|                          | degree                              | 2, 3, 4, 5, 6, 7                       |
|                          | gamma                               | scale, auto                            |
|                          | n_jobs                              | -1                                     |
| DecisionTreeClassifier   | criterion                           | gini, entropy                          |
|                          | splitter                            | best, random                           |
|                          | max_depth                           | None, 3, 5, 7, 9, 11, 13, 15, 17, 19   |
|                          | random_state                        | 0                                      |
| RandomForestClassifier   | n_estimators                        | 10, 50, 100, 200                       |
|                          | criterion                           | gini, entropy                          |
|                          | max_depth                           | None, 3, 5, 7, 9, 11, 13, 15, 17, 19   |
|                          | n_jobs                              | -1                                     |
|                          | random_state                        | 0                                      |

## Best Hyperparameters of Each Model
Best hyperparameters of each model based on validation recall. Details of hyperparameters tuning can be found on [Weights & Biases dashboard]().

| Models                   | Best Hyperparameters                | Validation Recall                      |
| ------------------------ | ----------------------------------- | -------------------------------------- |
| DummyClassifier          | random_state = 0                    | x%                                     |
|                          | strategy =                          |                                        |
| LogisticRegression       | random_state = 0                    | x%                                     |
|                          | C =                                 |                                        |
|                          | solver =                            |                                        |
|                          | n_jobs = -1                         |                                        |
| KNeighborsClassifier     | n_neighbors =                       | x%                                     |
|                          | weights =                           |                                        |
|                          | algorithm =                         |                                        |
|                          | p =                                 |                                        |
|                          | n_jobs = -1                         |                                        |
| SVC                      | C =                                 | x%                                     |
|                          | kernel =                            |                                        |
|                          | degree =                            |                                        |
|                          | gamma =                             |                                        |
|                          | n_jobs = -1                         |                                        |
| DecisionTreeClassifier   | criterion =                         | x%                                     |
|                          | splitter =                          |                                        |
|                          | max_depth =                         |                                        |
|                          | random_state = 0                    |                                        |
| RandomForestClassifier   | n_estimators =                      | x%                                     |
|                          | criterion =                         |                                        |
|                          | max_depth =                         |                                        |
|                          | n_jobs = -1                         |                                        |
|                          | random_state = 0                    |                                        |

## Performance of Each Model
Train each model with its best hyperparameters, and get its training and testing recall.

| Models                   | Training Recall                     | Testing Recall                         |
| ------------------------ | ----------------------------------- | -------------------------------------- |
| DummyClassifier          | x%                                  | x%                                     |
| LogisticRegression       | x%                                  | x%                                     |
| KNeighborsClassifier     | x%                                  | x%                                     |
| SVC                      | x%                                  | x%                                     |
| DecisionTreeClassifier   | x%                                  | x%                                     |
| RandomForestClassifier   | x%                                  | x%                                     |

## Best Performing Model
x is the best performing model because...