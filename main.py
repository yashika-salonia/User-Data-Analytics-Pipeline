from scripts.ingest import load_data
from scripts.transform import transform_data
from scripts.load import save_data
from scripts.analyze import analyze_data

raw_path = "data/raw_data.csv"
output_path = "output/processed_data.csv"

df = load_data(raw_path)
df = transform_data(df)
save_data(df, output_path)

analyze_data(output_path)