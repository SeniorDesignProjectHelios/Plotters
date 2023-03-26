import pandas as pd
import matplotlib.pyplot as plt


def plot_irradiance(file_name):
    # Custom date parser to combine date and time columns
    def custom_date_parser(date, time):
        return pd.to_datetime(date + ' ' + time, format='%Y/%m/%d %I:%M %p')

    # Read the CSV file and parse the 'DateTime' column
    data = pd.read_csv(file_name, parse_dates={'DateTime': ['Date', 'Time']}, date_parser=custom_date_parser)
    data.set_index("DateTime", inplace=True)

    # Column to plot
    column_to_plot = "Solar_w/m2"

    # Check if the column is present in the CSV file
    if column_to_plot in data.columns:
        # Plot the column against time
        data[column_to_plot].plot()
        plt.xlabel("Time")
        plt.ylabel("Solar_w/m2")
        plt.title("Solar_w/m2 vs Time")
        plt.show()
    else:
        print(f"Error: The specified column '{column_to_plot}' was not found in the CSV file.")


if __name__ == "__main__":
    file_name = input("Enter the CSV file name: ")
    plot_irradiance(file_name)
