import pandas as pd
import numpy as np

# Create a Series with ten random numbers
ser = pd.Series(np.random.randint(1, 100, 10))
print("Pandas Series:")
print(ser)

# Create a Series from a list
ser1 = pd.Series([10, 20, 30, 40, 50])
print("\nSeries from list:")
print(ser1)

# Create a Series with custom index
ser_custom = pd.Series([10, 20, 30, 40, 50],
                       index=['a', 'b', 'c', 'd', 'e'])
print("\nSeries with custom index:")
print(ser_custom)

# Create a DataFrame from a dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [24, 27, 22],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)
print("\nDataFrame:")
print(df)

# Selecting columns
print("\nSingle Column:")
print(df['Name'])

print("\nMultiple Columns:")
print(df[['Name', 'City']])

# Selecting rows using iloc and loc
print("\nFirst Row using iloc:")
print(df.iloc[0])

print("\nRow using loc:")
print(df.loc[1])

# Data Cleaning
df['Age'] = df['Age'].fillna(df['Age'].mean())
print("\nCleaned DataFrame:")
print(df)

# Create another DataFrame
data2 = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Salary': [25000, 30000, 28000]
}

df2 = pd.DataFrame(data2)

# Merging DataFrames
merged_df = pd.merge(df, df2, on='Name')
print("\nMerged DataFrame:")
print(merged_df)

# Aggregation
print("\nAge Aggregation:")
print(df['Age'].agg(['sum', 'mean', 'min', 'max']))

print("\nSalary Aggregation:")
print(merged_df['Salary'].sum())