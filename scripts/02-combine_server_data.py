import os
import pandas as pd
from datetime import datetime

def combine_csv_files(data_directory):
    csv_files = [file for file in os.listdir(data_directory) if file.endswith(".csv")]

    combined_data_frame = pd.DataFrame()

    for csv_file in csv_files:
        parts = csv_file.split("_")
        date_str = parts[1]
        timestamp_str = parts[2].split(".")[0]
        datetime_str = f"{date_str} {timestamp_str[:2]}:{timestamp_str[2:4]}:{timestamp_str[4:]}"

        csv_path = os.path.join(data_directory, csv_file)
        df = pd.read_csv(csv_path)

        df["DateTimestamp"] = datetime.strptime(datetime_str, "%Y%m%d %H:%M:%S")

        combined_data_frame = pd.concat([combined_data_frame, df], ignore_index=True)

        # Remove processed CSV file
        os.remove(csv_path)
        print(f"Processed and Deleted: {csv_file}")

    return combined_data_frame

def save_combined_data(combined_data_frame, output_file):
    if os.path.exists(output_file):
        previous_combined_data = pd.read_csv(output_file)
        appended_data_frame = pd.concat([previous_combined_data, combined_data_frame], ignore_index=True)
        appended_data_frame.to_csv(output_file, index=False)
    else:
        combined_data_frame.to_csv(output_file, index=False)

    print(f"Combined data saved to {output_file}")

def main():
    data_directory = os.path.join(os.path.dirname(__file__), "..", "servers-data")
    output_file = os.path.join("data", "master_combined.csv")

    combined_data_frame = combine_csv_files(data_directory)
    save_combined_data(combined_data_frame, output_file)

    file_list = os.listdir(data_directory)
    for file in file_list:
        if file.endswith(".csv"):
            file_path = os.path.join(data_directory, file)
            os.remove(file_path)
            print(f"Deleted: {file}")

if __name__ == "__main__":
    main()