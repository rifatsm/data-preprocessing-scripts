import os
import csv

def extract_max_submissions(input_file: str, output_file: str) -> None:
    """
    Reads a CSV file and extracts rows with max submissionNo for each userName.
    Writes the rows with max submissionNo for each userName to a new CSV file.

    Args:
        input_file (str): The name of the input CSV file.
        output_file (str): The name of the output CSV file.

    Returns:
        None
    """
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_file_path = os.path.join(script_dir, input_file)
    output_file_path = os.path.join(script_dir, output_file)

    # Dictionary to store the max submissionNo rows for each userName
    max_submissions = {}

    with open(input_file_path, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        
        # Iterate over each row in the input CSV file
        for row in reader:
            userName = row['userName']
            submissionNo = int(row['submissionNo'])
            
            # Check if userName already exists in the dictionary
            if userName in max_submissions:
                # Update the row if the current submissionNo is higher
                if submissionNo > int(max_submissions[userName]['submissionNo']):
                    max_submissions[userName] = row
            else:
                # Add userName and row to the dictionary if it doesn't exist
                max_submissions[userName] = row
    
    # Write the rows with max submissionNo for each userName to the output CSV file
    fieldnames = reader.fieldnames
    with open(output_file_path, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        
        # Iterate over the dictionary values and write the rows
        for row in max_submissions.values():
            writer.writerow(row)

# Specify the input and output file names
input_file = 'file_name.csv'
output_file = 'condensed_' + input_file

# Call the function to extract the rows with max submissionNo
extract_max_submissions(input_file, output_file)

print(f"Rows with max submissionNo for each userName have been extracted and saved in '{output_file}'.")
