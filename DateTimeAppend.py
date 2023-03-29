import csv
import os
from datetime import datetime

def process_csv(input_file):
    output_file = os.path.splitext(input_file)[0] + "DateTime" + os.path.splitext(input_file)[1]

    with open(input_file, "r") as infile, open(output_file, "w", newline="") as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        header = next(reader)
        header[0] = "DateTime"
        del header[1]
        writer.writerow(header)

        for row in reader:
            date_time_str = row[0] + " " + row[1]
            date_time_obj = datetime.strptime(date_time_str, "%m/%d/%Y %I:%M %p")
            row[0] = date_time_obj
            del row[1]
            writer.writerow(row)

    print(f"Processed CSV file saved as {output_file}")

if __name__ == "__main__":
    input_csv_file = input("Enter the name of your input CSV file: ")
    process_csv(input_csv_file)
