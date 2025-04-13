import pandas as pd
from data_collection.collect_data import load_data
def eda(df):
    """
    Perform Exploratory Data Analysis (EDA) on the given DataFrame.

    This function generates a variety of statistics and visualizations
    to help understand the distribution, missing values, and relationships
    in the data.

    Args:
        df (pd.DataFrame): The DataFrame containing the data to be analyzed.

    Returns:
        None
    """
    
    # 1. Show the first few rows of the data
    print("First 5 rows of the dataset:")
    print(df.head(), "\n")

    # 2. Summary statistics
    print("Summary statistics of the dataset:")
    print(df.describe(), "\n")

    # 3. Check for missing values
    print("Missing values in each column:")
    print(df.isnull().sum(), "\n")

    # 4. Display data types and general info
    print("Data types and info:")
    print(df.info(), "\n")

    # 5. Check the number of unique values in each column
    print("Unique values in each column:")
    print(df.nunique(), "\n")