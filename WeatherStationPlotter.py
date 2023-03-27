import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


def plot_irradiance_power(file_name):
    # Read the CSV file and parse the 'DateTime' column
    data = pd.read_csv(file_name, parse_dates=['DateTime'])
    data.set_index("DateTime", inplace=True)

    # Columns to plot
    columns_to_plot = ["Solar_w/m2", "Power"]

    # Check if all columns are present in the CSV file
    if all(column in data.columns for column in columns_to_plot):
        # Plot the columns against time
        ax = data[columns_to_plot].plot()

        # Format x-axis ticks and labels
        ax.xaxis.set_major_locator(mdates.AutoDateLocator())
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M'))
        plt.setp(ax.get_xticklabels(), rotation=30, ha='right')

        plt.xlabel("Time")
        plt.ylabel("Value")
        plt.title("Solar_w/m2 and Power vs Time")
        plt.legend(columns_to_plot)
        plt.grid(True)
        plt.show()
    else:
        print("Error: One or more of the specified columns were not found in the CSV file.")


if __name__ == "__main__":
    file_name = input("Enter the CSV file name: ")
    plot_irradiance_power(file_name)

# import pandas as pd
# import matplotlib.pyplot as plt
#
#
# def plot_irradiance_power(file_name):
#     # Custom date parser to combine date and time columns
#     def custom_date_parser(date, time):
#         return pd.to_datetime(date + ' ' + time, format='%Y/%m/%d %I:%M %p')
#
#     # Read the CSV file and parse the 'DateTime' column
#     data = pd.read_csv(file_name), parse_dates={'DateTime': ['Date', 'Time']}, date_parser=custom_date_parser)
#     data.set_index("DateTime", inplace=True)
#
#     # Columns to plot
#     columns_to_plot = ["Solar_w/m2", "Power"]
#
#     # Check if all columns are present in the CSV file
#     if all(column in data.columns for column in columns_to_plot):
#         # Plot the columns against time
#         data[columns_to_plot].plot()
#         plt.xlabel("Time")
#         plt.ylabel("Value")
#         plt.title("Solar_w/m2 and Power vs Time")
#         plt.legend(columns_to_plot)
#         plt.show()
#     else:
#         print("Error: One or more of the specified columns were not found in the CSV file.")
#
#
# if __name__ == "__main__":
#     file_name = input("Enter the CSV file name: ")
#     plot_irradiance_power(file_name)
