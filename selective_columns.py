import csv

def extract_data(input_file, output_file, column_name):
    """
    Extracts data from a CSV file based on a specified column name and writes the extracted data to another CSV file.

    Args:
        input_file (str): The path to the input CSV file.
        output_file (str): The path to the output CSV file.
        column_name (str): The name of the column to extract data from.

    Returns:
        None
    """
    with open(input_file, 'r') as file:
        reader = csv.DictReader(file)
        data = []
        
        for row in reader:
            data.append(reader.line_num - 1)
            data.append(row[column_name])
    
    # Write the extracted data to another CSV file
    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)
        
        # Write the header row
        writer.writerow(['uniqueId', column_name])

        # Write all the extracted data
        for i in range(0, len(data), 2):
            writer.writerow([data[i], data[i + 1]])

def example():
    # Example usage
    input_file = 'mnt/data_detailed/S23_P1_P_BigNumArithmetic.csv'
    output_file = 'mnt/data/S23_P1_P_BigNumArithmetic.csv'
    column_name = 'Correctness/Testing %'

    extract_data(input_file, output_file, column_name)

if __name__ == '__main__':
    example()

