import pandas as pd

def output_to_console(output):
    """
    This function is used to print output to console
    :arg: output (str)
    """
    print(output)

def output_to_file(output, file_path):
    """
    This function is used to write output to file
    :arg: output (str)
          file_path (str)
    :raises: FileNotFoundError: If file is not found
    """
    try:
        with open(file_path, 'w') as file:
            file.write(output)
    except FileNotFoundError:
        raise FileNotFoundError(f"File {file_path} not found")

def output_to_file_by_pandas(output, file_path):
    """
    This function is used to write output to file using pandas
    :arg: output (str)
          file_path (str)
    :raises: ValueError: If output is not pandas dataframe
    """
    if not isinstance(output, pd.DataFrame):
        raise ValueError("Output should be pandas dataframe")

    output.to_csv(file_path, index=False)
