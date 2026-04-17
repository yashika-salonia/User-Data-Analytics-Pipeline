import pandas as pd
import random

subjects = ["DSA", "DBMS", "OS", "CN", "AI"]

data = []

for i in range(1, 121):  # 120 rows (looks like big data)
    row = {
        "user_id": random.randint(1, 30),
        "session_time": random.randint(10, 120),
        "subject": random.choice(subjects),
        "distraction_count": random.randint(0, 10)
    }
    data.append(row)

df = pd.DataFrame(data)
df.to_csv("../data/raw_data.csv", index=False)

print("Fake dataset created with 120 rows")