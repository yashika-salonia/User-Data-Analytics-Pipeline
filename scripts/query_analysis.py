import sqlite3
import pandas as pd

def run_queries():
    conn = sqlite3.connect("database/analytics.db")

    # 1. Average session time per subject
    query1 = """
    SELECT subject, AVG(session_time) as avg_session
    FROM user_activity
    GROUP BY subject
    """

    df1 = pd.read_sql_query(query1, conn)

    # 2. Distraction impact
    query2 = """
    SELECT distraction_count, AVG(session_time) as avg_time
    FROM user_activity
    GROUP BY distraction_count
    """

    df2 = pd.read_sql_query(query2, conn)

    conn.close()

    return df1, df2