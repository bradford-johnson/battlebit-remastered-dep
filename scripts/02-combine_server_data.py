import os
import pandas as pd
from datetime import datetime

data_directory = os.path.join(os.path.dirname(__file__), "..", "servers-data")

csv_files = [file for file in os.listdir(data_directory) if file.endswith(".csv")]

combined_data_frame = pd.DataFrame()

for csv_file in csv_files:
    parts = csv_file.split("_")
    date_str = parts[1]
    timestamp_str = parts[2].split(".")[0]
    datetime_str = (
        f"{date_str} {timestamp_str[:2]}:{timestamp_str[2:4]}:{timestamp_str[4:]}"
    )

    csv_path = os.path.join(data_directory, csv_file)
    df = pd.read_csv(csv_path)

    df["DateTimestamp"] = datetime.strptime(datetime_str, "%Y%m%d %H:%M:%S")

    combined_data_frame = combined_data_frame._append(df, ignore_index=True)

output_file = os.path.join("data/master_combined.csv")
combined_data_frame.to_csv(output_file, index=False)

file_list = os.listdir(data_directory)

for file in file_list:
    if file.endswith(".csv"):
        file_path = os.path.join(data_directory, file)
        os.remove(file_path)
        print(f"Deleted: {file}")

print(f"Combined data saved to {output_file}")
