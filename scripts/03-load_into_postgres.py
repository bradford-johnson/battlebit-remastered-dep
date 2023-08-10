import pandas as pd
import psycopg2
from sqlalchemy import create_engine
import json


def normalize_column_name(name):
    """
    Normalize column names to lowercase with underscores instead of spaces or camel case

    Args:
        name (str): Column name to normalize

    Returns:
        str: Normalized column name

    Examples:
        >>> normalize_column_name("Column Name")
        "column_name"
    """
    name = "".join(["_" + c.lower() if c.isupper() else c for c in name]).lstrip("_")

    name = name.replace(" ", "_").lower()

    return name


with open("creds.json") as json_file:
    env_vars = json.load(json_file)

postgres_password = env_vars.get("DB_PASSWORD")

df = pd.read_csv("data/master_combined.csv")

df["DateTimestamp"] = (
    pd.to_datetime(df["DateTimestamp"]).dt.tz_localize(None).dt.tz_localize("UTC")
)

df.columns = [normalize_column_name(col) for col in df.columns]

db_connection = {
    "user": "postgres",
    "password": postgres_password,
    "host": "localhost",
    "port": "5432",
    "database": "postgres",
}

conn = psycopg2.connect(**db_connection)

engine = create_engine(
    f'postgresql://{db_connection["user"]}:{db_connection["password"]}@{db_connection["host"]}:{db_connection["port"]}/{db_connection["database"]}'
)

table_name = "battlebit_servers_by_hour"
df.to_sql(table_name, engine, index=False, if_exists="replace")

conn.close()
