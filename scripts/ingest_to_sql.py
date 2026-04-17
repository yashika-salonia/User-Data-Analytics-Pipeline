import pandas as pd
import sqlite3

def load_to_db(csv_path):
    df = pd.read_csv(csv_path)

    conn = sqlite3.connect("database/analytics.db")

    df.to_sql("user_activity", conn, if_exists="replace", index=False)

    print("Data loaded into SQLite DB")
    conn.close()