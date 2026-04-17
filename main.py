from scripts.ingest_to_sql import load_to_db
from scripts.query_analysis import run_queries
from scripts.visualize import plot_data

csv_path = "data/raw_data.csv"

load_to_db(csv_path)

df1, df2 = run_queries()

plot_data(df1, df2)