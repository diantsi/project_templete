import pandas as pd

def input_from_console():
    """
    This function is used to get input from console
     :return: str
    """
    return input("Enter the input: ")

def input_from_file(file_path):
    """
    This function is used to get input from file
    :arg: file_path (str)
    :return: str
    :raises: FileNotFoundError: If file is not found
    """
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"File {file_path} not found")

def input_from_file_by_pandas(file_path):
    """
    This function is used to get input from file using pandas
    :arg: file_path (str)
    :return: str
    :raises: FileNotFoundError: If file is not found
                 ValueError: If file is not csv
    """
    if not file_path.endswith('.csv'):
        raise ValueError("File should be csv")
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        raise FileNotFoundError(f"File {file_path} not found")

