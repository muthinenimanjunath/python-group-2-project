import pandas as pd
from data_collection.collect_data import load_data

def preprocess_data(df):
    """
    Cleans and preprocesses the raw dataset.

    Steps:
    - Removes rows with negative Quantity or UnitPrice
    - Handles missing CustomerID and Description
    - Extracts time-based features from InvoiceDate
    - Encodes categorical columns

    Args:
        df (pd.DataFrame): Raw input data

    Returns:
        pd.DataFrame: Cleaned and preprocessed data
    """

    # Remove rows with non-positive Quantity or UnitPrice
    df = df[(df['Quantity'] > 0) & (df['UnitPrice'] > 0)]

    # Drop rows where CustomerID or Description is missing
    df = df.dropna(subset=['CustomerID', 'Description'])

    # Convert CustomerID to integer
    df['CustomerID'] = df['CustomerID'].astype(int)

    # Convert InvoiceDate to datetime (in case it's not already)
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

    # Extract time features
    df['InvoiceMonth'] = df['InvoiceDate'].dt.to_period('M').astype(str)
    df['DayOfWeek'] = df['InvoiceDate'].dt.day_name()
    df['Hour'] = df['InvoiceDate'].dt.hour

    # Encode Country as category
    df['Country'] = df['Country'].astype('category').cat.codes

    return df