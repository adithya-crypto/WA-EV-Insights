# Name: Pavan Kalyan Divve

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import chi2_contingency


# Step 1: Initial Exploration
# Load the dataset
df = pd.read_csv("Electric_Vehicle_Population_Data.csv")

# Check for missing values
missing_values = df.isnull().sum()
print("Missing Values:\n", missing_values)

# Descriptive statistics
descriptive_stats = df.describe()
print("Descriptive Statistics:\n", descriptive_stats)

# Step 2: Data Cleaning and Preprocessing
# Drop irrelevant columns
df_cleaned = df.drop(
    ["VIN (1-10)", "DOL Vehicle ID", "Vehicle Location", "Postal Code"], axis=1
)

# Handle missing values in 'Electric Range'
df_cleaned["Electric Range"].fillna(df_cleaned["Electric Range"].mean(), inplace=True)


# Step 3: Exploratory Data Analysis (EDA)
# Geographic Distribution
plt.figure(figsize=(12, 6))
sns.countplot(
    x="County", data=df_cleaned, order=df_cleaned["County"].value_counts().index
)
plt.title("Distribution of Electric Vehicles Across Counties")
plt.xlabel("County")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.show()

# Vehicle Characteristics
plt.figure(figsize=(12, 6))
sns.countplot(x="Make", data=df_cleaned, order=df_cleaned["Make"].value_counts().index)
plt.title("Distribution of Electric Vehicles by Make")
plt.xlabel("Make")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.show()

# Scatter plot for Electric Range vs. Base MSRP
plt.figure(figsize=(10, 6))
sns.scatterplot(x="Electric Range", y="Base MSRP", data=df_cleaned)
plt.title("Scatter Plot: Electric Range vs. Base MSRP")
plt.xlabel("Electric Range")
plt.ylabel("Base MSRP")
plt.show()

# Step 4: Visualization (continue with relevant plots)

# Distribution of Electric Vehicle Types
plt.figure(figsize=(12, 6))
sns.countplot(
    x="Electric Vehicle Type",
    data=df_cleaned,
    order=df_cleaned["Electric Vehicle Type"].value_counts().index,
)
plt.title("Distribution of Electric Vehicle Types")
plt.xlabel("Electric Vehicle Type")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.show()

# Box plot for Electric Range by Vehicle Type
plt.figure(figsize=(12, 6))
sns.boxplot(x="Electric Vehicle Type", y="Electric Range", data=df_cleaned)
plt.title("Electric Range by Vehicle Type")
plt.xlabel("Electric Vehicle Type")
plt.ylabel("Electric Range")
plt.xticks(rotation=45)
plt.show()

# Descriptive statistics for Electric Range by Vehicle Type
electric_range_stats = df_cleaned.groupby("Electric Vehicle Type")[
    "Electric Range"
].describe()
print(
    "Descriptive Statistics for Electric Range by Vehicle Type:\n", electric_range_stats
)

# Step 6: Hypothesis Testing (if applicable)

# Chi-square test for independence between 'Electric Vehicle Type' and 'Clean Alternative Fuel Vehicle Eligibility'
contingency_table = pd.crosstab(
    df_cleaned["Electric Vehicle Type"],
    df_cleaned["Clean Alternative Fuel Vehicle (CAFV) Eligibility"],
)
chi2_stat, p_value, _, _ = chi2_contingency(contingency_table)

print("Chi-square Statistic:", chi2_stat)
print("P-Value:", p_value)
