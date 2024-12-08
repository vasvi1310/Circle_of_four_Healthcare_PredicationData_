import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv("medical_records.csv")

print("First few rows:")
print(data.head()) 

print("Column names:")
print(data.columns)

print("\nSummary statistics:")
print(data.describe(include='all'))

stroke_data = data[data['Disease_Category'] == 'Stroke']
print("Stroke data summary:")
print(stroke_data.describe(include='all'))

disease_stats = data.groupby('Disease_Category').describe(include='all')
print("Statistics by Disease Category:")
print(disease_stats)

sns.boxplot(
    x = "Disease_Category",
    y = "Age",
    data=data
)
plt.title('Distribution of Age by Disease Category')
plt.xlabel('Disease Category')
plt.ylabel('Age')
plt.xticks(rotation=45)  
plt.show()

sns.violinplot(
    x = "Disease_Category",
    y = "Age",
    data=data
)
plt.title('Distribution of Age by Disease Category (Violin Plot)')
plt.xlabel('Disease Category')
plt.ylabel('Age')
plt.xticks(rotation=45)
plt.show()
