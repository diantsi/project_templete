from app.io.input import input_from_console, input_from_file, input_from_file_by_pandas
from app.io.output import output_to_console , output_to_file, output_to_file_by_pandas


def main():
    console_val = input_from_console()
    file_val = input_from_file("input.txt")
    file_pandas_val = input_from_file_by_pandas("input.csv")

    output_to_console(console_val)
    output_to_console(file_val)
    output_to_console(file_pandas_val)

    output_to_file(console_val, "output.txt")
    output_to_file_by_pandas(file_pandas_val, "output.csv")


if __name__ == '__main__':
    main()
