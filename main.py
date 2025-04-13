from data_collection.collect_data import load_data
from data_processing.eda import eda
from data_processing.pre_process import preprocess_data
from database.create_db import main as insert_into_db
def main():
    """
    Main function to execute the data collection, preprocessing, and EDA.
    """
    
    print("Loading the dataset...")
    df = load_data()

    print("Preprocessing the dataset...")
    # Preprocess the data
    cleaned_df = preprocess_data(df)

    print("Inserting data into SQLite database...")
    # Insert data into the database
    insert_into_db(cleaned_df)
    
    print("Performing Exploratory Data Analysis (EDA)...")
    # Perform EDA
    eda(cleaned_df)

if __name__ == "__main__":
    main()