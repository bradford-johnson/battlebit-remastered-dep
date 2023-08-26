import pandas as pd
import psycopg2
from sqlalchemy import create_engine
import json
import pytz

with open("creds.json") as json_file:
    env_vars = json.load(json_file)

postgres_password = env_vars.get("DB_PASSWORD")


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

players_query = """

WITH players AS (
	SELECT
		date_timestamp AS date,
		region,
		COUNT(name) AS n_servers,
		SUM(max_players) AS player_capacity,
		SUM(players) AS total_players,
		SUM(queue_players) AS in_queue
	FROM
		battlebit_servers_by_hour
	WHERE
		is_official = TRUE
	GROUP BY
		date, region
	ORDER BY date ASC
)
SELECT
	*,
	total_players + in_queue AS total_online
FROM
	players

"""

df = pd.read_sql_query(players_query, engine)

conn.close()

df['date'] = pd.to_datetime(df['date'])

est_timezone = pytz.timezone('America/New_York')
df['date'] = df['date'].dt.tz_convert(est_timezone)

# WIP
print(df.head())
