# =========================================
# Unemployment Analysis in India with Python
# =========================================

# 1. Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 2. Load dataset
df = pd.read_csv("Unemployment in India.csv")
print("First 5 rows of data:")
print(df.head())
print("\nDataset Info:")
print(df.info())

# 3. Check for missing values
print("\nMissing values in each column:")
print(df.isnull().sum())

# 4. Convert date column to datetime (if available)
if 'Date' in df.columns:
    df['Date'] = pd.to_datetime(df['Date'])

# 5. Basic statistics
print("\nBasic Statistics:")
print(df.describe())

# 6. Plot unemployment rate by region/state
plt.figure(figsize=(12, 6))
sns.barplot(data=df, x='Region', y='Estimated Unemployment Rate (%)', ci=None)
plt.xticks(rotation=90)
plt.title("Unemployment Rate by Region")
plt.ylabel("Unemployment Rate (%)")
plt.xlabel("Region")
plt.show()

# 7. Trend over time (if date column exists)
if 'Date' in df.columns:
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=df, x='Date', y='Estimated Unemployment Rate (%)', hue='Region')
    plt.title("Unemployment Rate Trend Over Time")
    plt.ylabel("Unemployment Rate (%)")
    plt.xlabel("Date")
    plt.legend(title="Region", bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.show()

# 8. Heatmap of unemployment rate by region & date (optional)
if 'Date' in df.columns:
    pivot_data = df.pivot_table(index='Region', columns='Date', values='Estimated Unemployment Rate (%)')
    plt.figure(figsize=(14, 8))
    sns.heatmap(pivot_data, cmap='coolwarm', annot=False)
    plt.title("Heatmap of Unemployment Rate by Region Over Time")
    plt.show()
