import psycopg2
import pandas as pd

def get_rds_data():

    conn = psycopg2.connect(
        host="rds-endpoint",
        database="members",
        user="qa_user",
        password="password"
    )

    query = "SELECT * FROM members"

    df = pd.read_sql(query, conn)

    print("RDS rows:", len(df))

    return df