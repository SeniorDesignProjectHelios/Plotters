# import pandas as pd
# import matplotlib.pyplot as plt
#
# def plot_irradiance(file_name):
#     # Read the CSV file and parse the 'DateTime' column
#     data = pd.read_csv(file_name, parse_dates=['DateTime'])
#     data.set_index("DateTime", inplace=True)
#
#     # Columns to plot
#     columns_to_plot = ["Irradiance0", "Irradiance1", "Irradiance2", "Irradiance3"]
#
#     # Check if all columns are present in the CSV file
#     if all(column in data.columns for column in columns_to_plot):
#         # Plot the columns against time
#         data[columns_to_plot].plot()
#         plt.xlabel("Time")
#         plt.ylabel("Irradiance")
#         plt.title("Irradiance vs Time")
#         plt.legend(columns_to_plot)
#         plt.show()
#     else:
#         print("Error: One or more of the specified columns were not found in the CSV file.")
#
# if __name__ == "__main__":
#     file_name = input("Enter the CSV file name: ")
#     plot_irradiance(file_name)
#######################################################################################################################
# import pandas as pd
# import matplotlib.pyplot as plt
#
# def plot_irradiance(file_name):
#     # Read the CSV file and parse the 'DateTime' column
#     data = pd.read_csv(file_name, parse_dates=['DateTime'])
#     data.set_index("DateTime", inplace=True)
#
#     # Columns to plot
#     columns_to_plot = ["Irradiance0", "Irradiance1", "Irradiance2", "Irradiance3"]
#
#     # Check if all columns are present in the CSV file
#     if all(column in data.columns for column in columns_to_plot):
#         # Plot the columns against time
#         data[columns_to_plot].plot()
#         plt.xlabel("Time")
#         plt.ylabel("Irradiance")
#         plt.title("Irradiance vs Time")
#         plt.legend(columns_to_plot)
#         plt.show()
#     else:
#         print("Error: One or more of the specified columns were not found in the CSV file.")
#
# if __name__ == "__main__":
#     file_name = input("Enter the CSV file name: ")
#     plot_irradiance(file_name)
#######################################################################################################################
import pandas as pd
import matplotlib.pyplot as plt

def plot_irradiance_and_power(file_name):
    # Read the CSV file and parse the 'DateTime' column
    data = pd.read_csv(file_name, parse_dates=['DateTime'])
    data.set_index("DateTime", inplace=True)

    # Columns to plot
    irradiance_columns = ["Irradiance0", "Irradiance1", "Irradiance2", "Irradiance3"]
    power_columns = ["PowerPanel1", "PowerPanel2", "PowerTotal"]
    columns_to_plot = irradiance_columns + power_columns

    # Check if all columns are present in the CSV file
    if all(column in data.columns for column in columns_to_plot):
        # Plot the columns against time
        ax = data[irradiance_columns].plot()
        data[power_columns].plot(ax=ax, secondary_y=True)

        ax.set_xlabel("Time")
        ax.set_ylabel("Irradiance")
        ax.right_ax.set_ylabel("Power")
        ax.set_title("Irradiance and Power vs Time")

        lines = ax.get_lines() + ax.right_ax.get_lines()
        labels = [line.get_label() for line in lines]
        ax.legend(lines, labels, loc='best')

        plt.show()
    else:
        print("Error: One or more of the specified columns were not found in the CSV file.")

if __name__ == "__main__":
    file_name = input("Enter the CSV file name: ")
    plot_irradiance_and_power(file_name)
