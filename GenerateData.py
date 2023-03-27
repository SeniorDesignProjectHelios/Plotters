import pandas as pd
import numpy as np


def read_csv_file(file_name):
    data = pd.read_csv(file_name)
    return data


def generate_similar_data(data, column, multiplier):
    x = data[column]
    n = len(x)
    base_noise = np.random.rand(n) * 0.1  # Change the factor to adjust the randomness
    random_data = x * multiplier + base_noise * np.random.randn(n)
    return random_data


def save_to_csv(data, file_name):
    data.to_csv(file_name, index=False)


def main():
    file_name = input("Please enter the path to your .csv file: ")
    data = read_csv_file(file_name)

    print("Column names in the .csv file:")
    print(data.columns)

    column = input("Enter the column name to analyze: ")
    multiplier = float(input("Enter the multiplier value to scale the new data: "))

    similar_data = generate_similar_data(data, column, multiplier)
    new_column_name = input("Enter the name for the new column: ")

    data[new_column_name] = similar_data
    save_to_csv(data, file_name)
    print(f"Added the new column '{new_column_name}' to the .csv file.")


if __name__ == "__main__":
    main()
