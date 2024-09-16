import pandas as pd

# Load the dataset using a different encoding in case of issues
file_path = r'C:\Users\joshp\Downloads\SIS_Faculty-List.csv'
df = pd.read_csv(file_path, encoding='ISO-8859-1')

# Display the first few rows of the dataset for inspection
print(df.head())

# Check for missing values
print(df.isnull().sum())

# Check for duplicates
print(f'Duplicates: {df.duplicated().sum()}')

# Summary statistics to detect outliers
print(df.describe())

# Check data types
print(df.dtypes)
