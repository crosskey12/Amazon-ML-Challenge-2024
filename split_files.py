import pandas as pd
import os

# This code reads a specified CSV file, 
# splits it into a defined number of smaller CSV files, and saves these files in a designated output folder.


# Path to your CSV file
csv_file_path = './final_test.csv'

# Output folder
output_folder = './splitted_test_files'

# Number of splits
num_splits = 100 # Splitting test.csv into 100 testfiles for output to Mini-CPM model
# num_splits = 20 # Splitting the merged file (merged output of files from Mini-CPM model) into 20 testfiles for output to Gemma2 model


df = pd.read_csv(csv_file_path)
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Calculate the number of rows per split
rows_per_split = len(df) // num_splits
remainder = len(df) % num_splits

# Split the dataframe and save to CSV files
for i in range(num_splits):
    start_index = i * rows_per_split
    end_index = start_index + rows_per_split

    if i == num_splits - 1:
        end_index = len(df)
    
    split_df = df.iloc[start_index:end_index]

    split_file_name = os.path.join(output_folder, f'final_split_{i + 1}.csv')

    split_df.to_csv(split_file_name, index=False)
    
    print(f'Saved {split_file_name}')
