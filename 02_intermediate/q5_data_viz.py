# Q5: Data Visualization Dashboard
# Task: Create multiple chart types using matplotlib and seaborn
# Charts: heatmap, pie chart, line graph
# Dataset: Titanic from Kaggle (https://www.kaggle.com/c/titanic/data)
# Install: pip install seaborn matplotlib pandas

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset (download titanic.csv from Kaggle)
df = pd.read_csv("titanic.csv")

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle("Titanic Dataset Dashboard", fontsize=16)

# 1. Survival count bar chart
df["Survived"].value_counts().plot(
    kind="bar", ax=axes[0, 0], color=["steelblue", "orange"]
)
axes[0, 0].set_title("Survival Count")
axes[0, 0].set_xticklabels(["Died", "Survived"], rotation=0)

# 2. Passenger class pie chart
df["Pclass"].value_counts().plot(
    kind="pie", ax=axes[0, 1], autopct="%1.1f%%",
    labels=["Class 3", "Class 1", "Class 2"]
)
axes[0, 1].set_title("Passenger Class Distribution")

# 3. Age distribution line graph
df["Age"].dropna().sort_values().reset_index(drop=True).plot(
    ax=axes[1, 0], color="green"
)
axes[1, 0].set_title("Age Distribution")
axes[1, 0].set_xlabel("Passenger Index")
axes[1, 0].set_ylabel("Age")

# 4. Correlation heatmap
numeric_df = df[["Survived", "Pclass", "Age", "SibSp", "Parch", "Fare"]].dropna()
sns.heatmap(numeric_df.corr(), annot=True, fmt=".2f", ax=axes[1, 1], cmap="coolwarm")
axes[1, 1].set_title("Correlation Heatmap")

plt.tight_layout()
plt.savefig("titanic_dashboard.png")
print("Dashboard saved as titanic_dashboard.png")