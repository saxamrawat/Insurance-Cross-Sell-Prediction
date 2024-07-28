# Insurance Cross Sell Prediction

## Project Overview

This project aims to predict whether policyholders, who currently have health insurance with an insurance company, would be interested in purchasing vehicle insurance. The prediction model helps the company tailor its marketing strategies, improving customer outreach and optimizing revenue.

## Dataset Description

The dataset includes demographic information, vehicle details, and policy information for customers. It is divided into two parts:

### Train Data

| Variable             | Definition                                                                                          |
|----------------------|-----------------------------------------------------------------------------------------------------|
| `id`                 | Unique ID for the customer                                                                          |
| `Gender`             | Gender of the customer                                                                              |
| `Age`                | Age of the customer                                                                                 |
| `Driving_License`    | 0: Customer does not have a driving license, 1: Customer has a driving license                      |
| `Region_Code`        | Unique code for the region of the customer                                                          |
| `Previously_Insured` | 1: Customer already has Vehicle Insurance, 0: Customer doesn't have Vehicle Insurance               |
| `Vehicle_Age`        | Age of the vehicle                                                                                  |
| `Vehicle_Damage`     | 1: Customer's vehicle was damaged in the past, 0: No vehicle damage                                 |
| `Annual_Premium`     | The amount customer needs to pay as premium in the year                                             |
| `Policy_Sales_Channel` | Anonymized code for the channel of outreaching to the customer (e.g., agents, mail, phone, in-person) |
| `Vintage`            | Number of days the customer has been associated with the company                                    |
| `Response`           | 1: Customer is interested in vehicle insurance, 0: Customer is not interested                      |

### Test Data

The test data contains the same features as the train data, excluding the `Response` variable.

## Model Building

The goal is to build a machine learning model to predict the `Response` variable (1: Interested, 0: Not Interested) based on the provided features. Key steps include:

1. **Data Preprocessing**: Handling missing values, encoding categorical variables, scaling features, etc.
2. **Feature Engineering**: Creating new features or modifying existing ones to improve model performance.
3. **Model Selection**: Choosing appropriate algorithms and tuning hyperparameters.
4. **Evaluation**: Assessing model performance using metrics like accuracy, precision, recall, and F1 score.

## AWS Deployment

The model is deployed on AWS to enable scalable and reliable predictions. You can access the deployment via the following links:

- **Deployment Link: http://crosssellprediction-env.eba-dummta2v.ap-southeast-2.elasticbeanstalk.com/

## Getting Started

To get started with the project, clone the repository and follow the setup instructions:

```bash
git clone https://github.com/saxamrawat/Insurance-Cross-Sell-Prediction.git
cd Insurance-Cross-Sell-Prediction
