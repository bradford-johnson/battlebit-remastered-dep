import requests
import pandas as pd
from datetime import datetime
import os

url = "https://publicapi.battlebit.cloud/Servers/GetServerList"

directory = "servers"

try:
    response = requests.get(url)

    if response.status_code == 200:
        json_data = response.json()

        df = pd.DataFrame(json_data)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        filename = os.path.join(directory, f"data_{timestamp}.csv")

        df.to_csv(filename, index=False)

        print("Saved data as:", filename)
    else:
        print("Request failed with status code:", response.status_code)
except requests.exceptions.RequestException as e:
    print("Request error:", e)

try:
    print("Current working directory:", os.getcwd())

    print("Absolute path of the filename:", os.path.abspath(filename))

    df.to_csv(filename, index=False)

    print("Saved data as:", filename)
except Exception as e:
    print("error", e)
