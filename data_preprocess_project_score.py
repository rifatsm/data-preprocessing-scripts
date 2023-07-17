import os
from selective_columns import extract_data

def list_files(directory):
    """
    This function takes a directory path as input and returns a list of all the files in the directory and its subdirectories.
    For each file, it also extracts selective columns and saves the output to a new file in the 'mnt/data/' directory.

    Args:
    - directory (str): The path of the directory to search for files.

    Returns:
    - file_list (list): A list of all the files in the directory and its subdirectories.
    """
    file_list = []
    output_file_path = 'mnt/data/'
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            output_file = output_file_path + file
            extract_data(file_path, output_file, 'Correctness/Testing %')
            file_list.append(file_path)

    return file_list

def preprocess_for_project_score():
    """
    This function is an example usage of the list_files() function.
    It takes a directory path as input, calls the list_files() function to get a list of all the files in the directory and its subdirectories,
    and then prints the list of files.

    Args:
    - None

    Returns:
    - None
    """
    directory_path = 'mnt/data_detailed'

    files = list_files(directory_path)

    # Print the list of files
    for file in files:
        print(file)

if __name__ == '__main__':
    preprocess_for_project_score()
