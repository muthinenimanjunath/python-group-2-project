# DAB111: Group Project - Online Retail Data

## Project Overview

This project involves storing and presenting transactional retail data through a web application. The dataset contains all transactions occurring between 01/12/2010 and 09/12/2011 for a UK-based online retailer. The data is stored in a SQLite database and is served via a Flask web application. The user can view, add, and search records in the database through a web interface.

### Features
- **Data Collection**: The project loads a dataset from a CSV file containing online retail transactions.
- **Data Preprocessing**: The data is cleaned and prepared for storage in a SQLite database.
- **Database**: The data is stored in an SQLite database and can be accessed via Flask.
- **Web Interface**: A basic web interface is provided for users to view, search, and add records to the database.

## Project Structure

group-2-project/
│
├── data_collection/           # Contains scripts for data collection and loading
│
├── data_processing/           # Scripts for data preprocessing and cleaning
│
├── database/                  # Contains database creation and interaction scripts
│
├── website/                   # Flask web application
│   ├── static/                # Contains CSS and other static files
│   ├── templates/             # HTML templates for web pages
│   │   ├── about.html         # About page
│   │   ├── add_data.html      # Add data page
│   │   ├── data.html          # Data page displaying the records
│   │   └── index.html         # Index page (Homepage)
│   └── app.py                 # Main Flask application script
│
├── Readme.md                  # This file (Project documentation)
├── requirements.txt           # Python dependencies (for installing necessary packages)

## Setup and Installation

1. **Clone the Repository:**

   ```bash
   git clone <repository_url>
   cd <project_folder>
   ```

2. **Set Up a Virtual Environment (Optional, but Recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scripts\activate
   ```

3. **Install the Dependencies:**

   If you haven't already installed the dependencies, you can install them using:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Data Setup (main.py):**

   Before running the web application, make sure to set up the database and load the data by running the `main.py` script:

   ```bash
   python main.py
   ```

   This script will handle the data processing and insert the necessary data into the SQLite database.

5. **Run the Flask Application (app.py):**

   Once the data is set up, navigate to the `website` folder and run the Flask server with the following command:

   ```bash
   python app.py
   ```

   The application should now be running at `http://localhost:5000`.

   **Note:** If you've already run `main.py` before and the database is set up, you can directly start the Flask server by running `app.py`.

## Functionality

The project provides the following functionality:

- **View Data**: Users can view all the transactional data stored in the database through the `data.html` page.
- **Add Data**: Users can add new records to the database via the `add_data.html` page. After adding data, the user is redirected to the data page to view the newly added record.
- **About Page**: The `about.html` page provides information about the dataset, including the source and variable definitions.

## About the Dataset

The dataset used in this project contains transactional data from an online retail store. The data spans from 01/12/2010 to 09/12/2011 and includes the following fields:

- **InvoiceNo**: Invoice number. A 6-digit integral number uniquely assigned to each transaction.
- **StockCode**: Product (item) code. A 5-digit integral number uniquely assigned to each distinct product.
- **Description**: Product name.
- **Quantity**: The quantities of each product (item) per transaction.
- **InvoiceDate**: The date and time when each transaction was generated.
- **UnitPrice**: Product price per unit in GBP.
- **CustomerID**: A 5-digit integral number uniquely assigned to each customer.
- **Country**: The country where each customer resides.

## Technologies Used

- **Python**: For data processing, database interaction, and the web application.
- **Flask**: A micro web framework used to serve the data.
- **SQLite**: A lightweight relational database for storing transactional data.
- **HTML/CSS**: For the frontend web interface.

## Contribution

This is a group project for the DAB111 course. Contributions are made by multiple team members, and the code is hosted in a shared GitHub repository.

## License

This project is licensed under the MIT License.
