import os
import pandas as pd
import matplotlib.pyplot as plt
# Assuming the CSV file is named 'data.csv' and is in the same folder as your code
script_directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_directory)

file_path = 'data.csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(file_path)

# Display the first few rows of the DataFrame
print(df.head())

# Get information about the columns and data types
print(df.info())

# Get summary statistics for numeric columns
print(df.describe())


