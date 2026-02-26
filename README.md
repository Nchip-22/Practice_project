# Customer Churn Analysis Project
This project focuses on analyzing customer churn data to identify the key factors that influence customers to leave a service. The analysis uses data visualization techniques with Python.
## Data Overview
This project uses a dataset from the file Churn_Modelling.csv, which contains customer behavior information such as country, number of products used, age, and activity status.
### Basic statistics of the dataset:
* Retained: 7,963 customers
* Exited: 2,037 customers
### Data Source
* **Dataset:** [Customer Churn Analysis Dataset](https://www.kaggle.com/datasets/sidramazam/customer-churn-analysis-dataset/data)
* **Platform:** Kaggle
* **Author:** Sidra Mazam
## Key Insights

### 1. Geography & Market Analysis
* **Germany** is the highest-risk market with an overall churn rate of **32.44%**.
* In contrast, **France** and **Spain** show much lower churn rates at 16.15% and 16.67% respectively.

### 2. Number of Products
The number of products a customer owns is a critical predictor of churn:
* **Extreme Risk:** Customers with **4 products** have a **100% churn rate** across all regions.
* **Highest Loyalty:** Customers with **2 products** are the most stable group, with a churn rate of only **7.58%**.

### 3. Age Distribution
* The analysis reveals a clear trend where customers aged **40–60 years** have the highest density of churn, marking them as a key demographic for retention efforts.

### 4. Active Member Status
Activity status is a major factor in customer retention:
* **Inactive Members** are significantly more likely to leave than active ones in every country.
* **Germany Focus:** Inactive customers in Germany show a particularly high churn rate of **41.08%**, compared to 23.72% for active members in the same country.

### 5. Recommendations

**Focus on Germany**
Investigate why German customers are unhappy. Determine whether the issue is stronger competition in the market or poor service quality in that region.

**Address Product Complexity**
The data suggests that customers with too many products may be experiencing issues or dissatisfaction due to complex services. The bank should focus on better supporting customers who hold 3–4 products.

**Re-engage Inactive Members**
Use personalized promotions to re-engage inactive customers and encourage more consistent usage.

**Target Older Customers**
Develop special loyalty programs or tailored financial products specifically for customers aged 45 and above


## Tools & Libraries
* **Python** – Main programming language for the analysis.
* **Pandas** – For data cleaning and data manipulation.
* **Seaborn & Matplotlib** – For creating data visualizations.