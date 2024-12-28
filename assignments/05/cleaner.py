import pandas as pd

# Load the CSV file to examine its contents
file_path = 'lotr_scripts.csv'
lotr_data = pd.read_csv(file_path)

# Drop the unnecessary 'Unnamed: 0' column
lotr_data_cleaned = lotr_data.drop(columns=['Unnamed: 0'])

# Remove leading/trailing whitespaces from 'char', 'dialog', and 'movie'
lotr_data_cleaned = lotr_data_cleaned.apply(lambda col: col.str.strip() if col.dtypes == 'object' else col)

# Save the cleaned dataset
cleaned_file_path = 'lotr_scripts_cleaned.csv'
lotr_data_cleaned.to_csv(cleaned_file_path, index=False)