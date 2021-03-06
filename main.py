import pandas as pd
import sqlite3

conn = sqlite3.connect("SQLite.db")
cur = conn.cursor()
csvfiles = ["data/feed_station_mapping (1).csv", "data/consumptions (1).csv"]
table_name = ["feed_station_mapping", "consumptions"]

for csv, table in zip(csvfiles, table_name):
    df = pd.read_csv(csv)
    df.to_sql(table, conn, if_exists='fail', index=False)
