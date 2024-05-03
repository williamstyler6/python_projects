import pandas as pd

# Create a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emily'],
    'Age': [25, 30, 35, 40, 45],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Boston'],
    'Salary': [50000, 60000, 70000, 80000, 90000]
}

df = pd.DataFrame(data)

# Display the DataFrame
print("Original DataFrame:")
print(df)
print()

# Practice tasks

# Task 1: Selecting a column
print("Task 1: Selecting a column - Name")
print(df['Name'])
print()

# Task 2: Filtering rows based on condition
print("Task 2: Filtering rows based on condition - Age > 30")
print(df[df['Age'] > 30])
print()

# Task 3: Adding a new column
print("Task 3: Adding a new column - Senior")
df['Senior'] = df['Age'] > 35
print(df)
print()

# Task 4: Sorting DataFrame
print("Task 4: Sorting DataFrame by Salary")
print(df.sort_values(by='Salary', ascending=False))
print()

# Task 5: Grouping and Aggregating
print("Task 5: Grouping and Aggregating - Average Salary by City")
print(df.groupby('City')['Salary'].mean())
print()

# Task 6: Handling missing values (Adding missing data for illustration)
import numpy as np
df.loc[2, 'Salary'] = np.nan
print("Task 6: Handling missing values - Filling NaN with Mean Salary")
print(df.fillna(df['Salary'].mean()))
print()

# Task 7: Deleting a column
print("Task 7: Deleting a column - Senior")
df.drop('Senior', axis=1, inplace=True)
print(df)
print()
