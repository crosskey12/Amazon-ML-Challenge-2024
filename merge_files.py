
import os
import pandas as pd


# This code creates a new CSV file with same features as the input CSV, 
# then updates the predictions by reading from multiple CSV files in a specified folder, 
# and saves the results to the output CSV.

def create_empty_prediction_csv(input_csv_path, output_csv_path):
    df = pd.read_csv(input_csv_path)
    new_df = pd.DataFrame({'index': df['index'], 'prediction': ''})
    new_df.to_csv(output_csv_path, index=False)

# Function to update predictions from files in a folder
def update_predictions_from_folder(folder_path, output_csv_path):
    result_df = pd.read_csv(output_csv_path)
    
    for filename in os.listdir(folder_path):
        if filename.endswith(".csv"):
            file_path = os.path.join(folder_path, filename)
            df = pd.read_csv(file_path)

            for idx, row in df.iterrows():
                result_df.loc[result_df['index'] == row['index'], 'prediction'] = row['prediction']
    
    result_df.to_csv(output_csv_path, index=False)

# Example usage:
input_csv_path = "./test.csv"

# ORIGINAL
output_csv_path = './final_predictions.csv'
folder_path = './4/Amazon ML Challenge Final Output Test Files'  # Replace with the actual folder path

# Create an empty prediction CSV
create_empty_prediction_csv(input_csv_path, output_csv_path)

# Update predictions from the folder
update_predictions_from_folder(folder_path, output_csv_path)

print('Done')