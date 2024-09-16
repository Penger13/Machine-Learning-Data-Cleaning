import pandas as pd

# Load the dataset
file_path = r'C:\Users\joshp\Downloads\SIS_Faculty-List.csv'
df = pd.read_csv(file_path, encoding='ISO-8859-1')

# Clean column names by removing newline characters
df.columns = df.columns.str.replace('\n', '').str.strip()

# Convert columns to numeric where appropriate
for col in df.columns:
    try:
        df[col] = pd.to_numeric(df[col])
    except (ValueError, TypeError):
        pass  # Keep original data if conversion fails

# Identify numeric columns
numeric_cols = df.select_dtypes(include=['number']).columns

# Fill missing values in numeric columns with their mean
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())

# Handle missing values for categorical columns
categorical_columns = ['Location', 'Highest Qualification', 'University', 'Major']
for col in categorical_columns:
    if col in df.columns:
        df[col] = df[col].fillna(df[col].mode()[0])

# Forward fill for missing 'JoinDate' and 'LWD'
df['JoinDate'] = df['JoinDate'].ffill()
df['LWD'] = df['LWD'].bfill()

# Convert 'JoinDate' and 'LWD' to datetime format
df['JoinDate'] = pd.to_datetime(df['JoinDate'], format='%d-%b-%y', errors='coerce')
df['LWD'] = pd.to_datetime(df['LWD'], format='%d-%b-%y', errors='coerce')

# Drop rows with invalid 'JoinDate' or 'LWD'
df_cleaned = df.dropna(subset=['JoinDate', 'LWD'])

# Save the cleaned dataset
df_cleaned.to_csv('cleaned_SIS_Faculty_List.csv', index=False)

print("Data cleaning complete. The cleaned dataset has been saved.")
