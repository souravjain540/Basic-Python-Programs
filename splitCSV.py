import pandas as pd

# Load your dataset
df = pd.read_csv('yourCSV.csv')

# Define the number of rows for each file
rows_per_file = 5000

# Calculate the number of files
num_files = 10

# Split the data and write to files
for i in range(num_files):
    start = i * rows_per_file
    end = (i + 1) * rows_per_file
    df[start:end].to_csv(f'output_file_{i+1}.csv', index=False)
