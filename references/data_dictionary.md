# Data Dictionary

## 1. telco_customer.csv
This is raw dataset downloaded from [Kaggle](https://www.kaggle.com/blastchar/telco-customer-churn). It has 7,043 instances and 21 attributes.

| Attributes                | Data Types  | Descriptions                                                                  |
| ------------------------- | ------------| -----------------------------------------------------------------------------| 
| customerID                | object      | Customer ID                                                                   |
| gender                    | object      | Whether the customer is a male or a female (Male, Female)                     |
| SeniorCitizen             | int64       | Whether the customer is a senior citizen or not (1, 0)                        |
| Partner                   | object      | Whether the customer has a partner or not (Yes, No)                           |
| Dependents                | object      | Whether the customer has dependents or not (Yes, No)                          |
| tenure                    | int64       | Number of months the customer has stayed with the company                     |
| PhoneService              | object      | Whether the customer has a phone service or not (Yes, No)                     |
| MultipleLines             | object      | Whether the customer has multiple lines or not (Yes, No, No phone service)    |
| InternetService           | object      | Customer’s internet service provider (DSL, Fiber optic, No)                   |
| OnlineSecurity            | object      | Whether the customer has online security or not (Yes, No, No internet service)|
| OnlineBackup              | object      | Whether the customer has online backup or not (Yes, No, No internet service)  |
| DeviceProtection          | object      | Whether the customer has device protection or not (Yes, No, No internet service) |
| TechSupport               | object      | Whether the customer has tech support or not (Yes, No, No internet service)   |
| StreamingTV               | object      | Whether the customer has streaming TV or not (Yes, No, No internet service)   |
| StreamingMovies           | object      | Whether the customer has streaming movies or not (Yes, No, No internet service) |
| Contract                  | object      | The contract term of the customer (Month-to-month, One year, Two year)        |
| PaperlessBilling          | object      | Whether the customer has paperless billing or not (Yes, No)                   |
| PaymentMethod             | object      | The customer’s payment method (Electronic check, Mailed check, Bank transfer (automatic), Credit card (automatic)) |
| MonthlyCharges            | float64     | The amount charged to the customer monthly                                    |
| TotalCharges              | object      | The total amount charged to the customer since subscription                   |
| Churn                     | object      | Whether the customer churned or not (Yes, No)                                 |

## 2. telco_customer_cleaned.csv
This is transformed dataset after data cleaning. It has 7,043 instances and 19 attributes. All categorical features are then being one-hot encoded.

| Attributes                | Data Types  | Descriptions                                                                  |
| ------------------------- | ------------| -----------------------------------------------------------------------------| 
| gender                    | object      | Whether the customer is a male or a female (Male, Female)                     |
| SeniorCitizen             | object      | Whether the customer is a senior citizen or not (Yes, No)                     |
| Partner                   | object      | Whether the customer has a partner or not (Yes, No)                           |
| Dependents                | object      | Whether the customer has dependents or not (Yes, No)                          |
| tenure                    | int64       | Number of months the customer has stayed with the company                     |
| PhoneService              | object      | Whether the customer has a phone service or not (Yes, No)                     |
| MultipleLines             | object      | Whether the customer has multiple lines or not (Yes, No, No phone service)    |
| InternetService           | object      | Customer’s internet service provider (DSL, Fiber optic, No)                   |
| OnlineSecurity            | object      | Whether the customer has online security or not (Yes, No, No internet service)|
| OnlineBackup              | object      | Whether the customer has online backup or not (Yes, No, No internet service)  |
| DeviceProtection          | object      | Whether the customer has device protection or not (Yes, No, No internet service) |
| TechSupport               | object      | Whether the customer has tech support or not (Yes, No, No internet service)   |
| StreamingTV               | object      | Whether the customer has streaming TV or not (Yes, No, No internet service)   |
| StreamingMovies           | object      | Whether the customer has streaming movies or not (Yes, No, No internet service) |
| Contract                  | object      | The contract term of the customer (Month-to-month, One year, Two year)        |
| PaperlessBilling          | object      | Whether the customer has paperless billing or not (Yes, No)                   |
| PaymentMethod             | object      | The customer’s payment method (Electronic check, Mailed check, Bank transfer (automatic), Credit card (automatic)) |
| MonthlyCharges            | float64     | The amount charged to the customer monthly                                    |
| Churn                     | object      | Whether the customer churned or not (1, 0)                                    |