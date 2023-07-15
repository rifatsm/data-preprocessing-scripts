"""
This script reads a CSV file containing a 'userName' column and adds a new 'uniqueId' column to the file. The 'uniqueId' column contains a unique number for each unique 'userName' value in the original file. The updated CSV file is saved with a 'anon_' prefix in the same directory as the original file.

Functions:
----------
add_unique_numbers(file_name):
    Reads a CSV file and adds a new 'uniqueId' column to the file. The 'uniqueId' column contains a unique number for each unique 'userName' value in the original file. The updated CSV file is saved with a 'anon_' prefix in the same directory as the original file.

    Parameters:
    -----------
    file_name : str
        The name of the CSV file to read and update.

    Returns:
    --------
    None
"""
import os
import csv

def add_unique_numbers(file_name):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, file_name)
    
    # Dictionary to store mapping of userName to unique numbers
    user_numbers = {}
    
    # Prepare the new file path
    anon_file_name = 'anon_' + file_name
    anon_file_path = os.path.join(script_dir, anon_file_name)
    
    with open(file_path, 'r') as file, open(anon_file_path, 'w', newline='') as anon_file:
        reader = csv.reader(file)
        writer = csv.writer(anon_file)
        header = next(reader)  # Read the header row
        
        # Find the index of the 'userName' column
        user_name_index = header.index('userName')
        
        # Remove the 'userName' column from the header
        header.pop(user_name_index)
        
        # Insert 'UniqueNumber' as the first column in the header
        header.insert(0, 'uniqueId')
        
        # Write the updated header to the new file
        writer.writerow(header)
        
        # Generate unique numbers for each unique userName and write the updated rows to the new file
        for row in reader:
            user_name = row.pop(user_name_index)
            if user_name not in user_numbers:
                user_numbers[user_name] = len(user_numbers) + 1
            row.insert(0, str(user_numbers[user_name]))
            
            # Write the updated row to the new file
            writer.writerow(row)
            
    print(f"New CSV file '{anon_file_name}' has been created.")

# Example usage
csv_file_name = 'file_name.csv'
add_unique_numbers(csv_file_name)
