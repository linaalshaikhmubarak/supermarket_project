import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("data/supermarket_sales.csv")

# Data cleaning: convert 'Date' to datetime
df['Date'] = pd.to_datetime(df['Date'])

# 1. Total Sales by Branch (Bar Chart)
plt.figure(figsize=(8, 6))
df.groupby('Branch')['Sales'].sum().plot(kind='bar')
plt.title('Total Sales by Branch')
plt.xlabel('Branch')
plt.ylabel('Total Sales')
plt.tight_layout()
plt.savefig('images/branch_sales.png', dpi=300)
plt.close()

# 2. Payment Methods Distribution (Pie Chart)
plt.figure(figsize=(8, 6))
df.groupby('Payment')['Sales'].sum().plot(
    kind='pie', autopct='%1.1f%%', startangle=90)
plt.title('Payment Methods Distribution')
plt.ylabel('')
plt.tight_layout()
plt.savefig('images/payment_methods.png', dpi=300)
plt.close()

# 3. Daily Sales Trend (Line Chart)
daily_sales = df.groupby('Date')['Sales'].sum()

plt.figure(figsize=(10, 6))
daily_sales.plot(kind='line')
plt.title('Daily Sales Trend')
plt.xlabel('Date')
plt.ylabel('Total Sales')
plt.tight_layout()
plt.savefig('images/daily_trend.png', dpi=300)
plt.close()

# 4. Define functions for analysis


def average_sales(df):
    """Calculate the average sales."""
    return df['Sales'].mean()


def total_sales_by_branch(df, branch):
    """Calculate total sales for a given branch."""
    return df[df['Branch'] == branch]['Sales'].sum()


# 5. Print basic statistics
print("Average sales across all branches:", average_sales(df))
print("Total sales for branch Cairo:", total_sales_by_branch(df, 'Cairo'))
