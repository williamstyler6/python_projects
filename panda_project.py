import pandas as pd

def main():
    # Load the CSV file into a DataFrame
    df = pd.read_csv('practice_data.csv')

    # Display the DataFrame
    print("Original DataFrame:")
    print(df)
    print()

    # Display basic statistics
    print("Basic Statistics:")
    print(df.describe())
    print()

    # Filter data
    print("Filtered Data (Age < 35):")
    filtered_df = df[df['Age'] < 35]
    print(filtered_df)
    print()

    # Add a new column
    df['Bonus'] = df['Salary'] * 0.1

    # Display the DataFrame with the new column
    print("DataFrame with Bonus column:")
    print(df)
    print()

    # Group by Age and calculate average salary
    print("Average Salary by Age:")
    average_salary_by_age = df.groupby('Age')['Salary'].mean()
    print(average_salary_by_age)
    print()

    # Save DataFrame to a CSV file
    df.to_csv('output.csv', index=False)
    print("DataFrame saved to output.csv")

if __name__ == "__main__":
    main()
