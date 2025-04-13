import sqlite3
from pathlib import Path

def create_connection(db_path="database/retail_sales.db"):
    db_file = Path(__file__).resolve().parent.parent / db_path
    print(f"Database will be created at: {db_file}") 
    return sqlite3.connect(db_file)

def create_table(conn):
    query = """
    CREATE TABLE IF NOT EXISTS sales (
        InvoiceNo TEXT,
        StockCode TEXT,
        Description TEXT,
        Quantity INTEGER,
        InvoiceDate TEXT,
        UnitPrice REAL,
        CustomerID INTEGER,
        Country INTEGER,
        InvoiceMonth TEXT,
        DayOfWeek TEXT,
        Hour INTEGER
    );
    """
    conn.execute(query)
    conn.commit()

def insert_data(conn, df):
    df.to_sql("retail_sales", conn, if_exists="replace", index=False)

def main(df):
    conn = create_connection()
    create_table(conn)
    insert_data(conn, df)
    print("Data inserted into the database.")
    conn.close()