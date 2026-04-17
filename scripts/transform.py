def transform_data(df):
    df["focus_score"] = df["session_time"] - (df["distraction_count"] * 5)

    # remove noise
    df = df[df["focus_score"] > 0]

    print("Data Transformed:", df.shape)
    return df