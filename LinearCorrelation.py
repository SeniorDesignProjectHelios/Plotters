import pandas as pd
from scipy.stats import pearsonr


def read_csv_file(file_name):
    data = pd.read_csv(file_name, parse_dates=[0])
    return data


def calculate_correlation(data, column1, column2):
    x = data[column1]
    y = data[column2]
    correlation_coefficient, _ = pearsonr(x, y)
    return correlation_coefficient


def main():
    file_name = input("Please enter the path to your .csv file: ")
    data = read_csv_file(file_name)
    column1 = "Irradiance"
    column2 = "PowerTotal"

    correlation_coefficient = calculate_correlation(data, column1, column2)
    print(f"Correlation coefficient between {column1} and {column2}: {correlation_coefficient:.4f}")


if __name__ == "__main__":
    main()
