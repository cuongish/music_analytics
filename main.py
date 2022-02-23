import pandas
import sqlite3

conn = sqlite3.connect("SQLite.db")
cur = conn.cursor()
csvfile = "feed_station_mapping.csv"
table_name = "feed_station_mapping"

df = pandas.read_csv(csvfile)
df.to_sql(table_name, conn, if_exists='fail', index=False)
