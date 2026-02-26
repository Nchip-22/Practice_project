import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

df = pd.read_csv(r"Data\Churn_Modelling.csv")

#Chart 1: Number of Retained and Exited Customers

Churn_count = df[df['Exited'] == 1]
Retained = df[df['Exited'] == 0]
count = df["Exited"].value_counts().sort_index()
count.index = count.index.map({0: "Retained", 1: "Exited"})

total = count.sum()
percentages = (count / total) * 100

bars = plt.bar(count.index, count.values,color=["cornflowerblue", "salmon"])

plt.title("Customer Status Overview")
plt.xlabel("Status")
plt.ylabel("Count")
plt.bar_label(bars, labels=[f"{p:.1f}%" for p in percentages])
plt.show()


print(("Exited = "),len(Churn_count))
print(("Retained = "),len(Retained))

#Chart 2: Customer Churn by Geography: Highest-Churn Country

geography_churn = df.groupby('Geography')['Exited'].mean() * 100
geography_churn_percent = geography_churn.map(lambda x: f"{x:.2f}%")
print(" Churn rate by Geography")
print(geography_churn_percent)

## Customer Churn by Geography and Active Customers
active_churn = df.groupby(['IsActiveMember', 'Geography'])['Exited'].mean() * 100
active_churn = active_churn.map(lambda x: f"{x:.2f}%")
print(active_churn.unstack())

p_chart2 = sns.barplot(data=df, x='Geography', y=df['Exited']*100, hue='IsActiveMember', errorbar=None, palette=["salmon", "cornflowerblue"])

for container in p_chart2.containers:
    p_chart2.bar_label(container, fmt="%.1f%%")

plt.title('Churn Rate by Geography & Active Status')
plt.ylabel('Churn Rate (%)')
plt.legend(title='Active Member')
plt.show()

#Chart 3: Customer Churn by Number of Products
product_churn = df.groupby('NumOfProducts')['Exited'].mean() * 100
product_churn_percent = product_churn.map(lambda x: f"{x:.2f}%")
print("Churn rate by Numbers of product")
print(product_churn_percent)

chart = pd.crosstab(df["NumOfProducts"],df["Exited"],normalize="index")*100
p_chart3=chart.plot(kind="bar",color=("cornflowerblue","salmon"))

for container in p_chart3.containers:
    p_chart3.bar_label(container, fmt="%.1f%%")

plt.title("percentage of Exited by Number of product")
plt.ylabel("percentage of Exited")
plt.xlabel("Number of product")
plt.show()

# Chart 4: Customer Churn by Age Group
sns.kdeplot(df[df['Exited'] == 0]['Age'], fill=True, label='Retained', color='cornflowerblue')
sns.kdeplot(df[df['Exited'] == 1]['Age'], fill=True, label='Exited', color='salmon')

plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Density')
plt.legend()
plt.show()


