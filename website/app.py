from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os
from pathlib import Path

app = Flask(__name__)

# Database connection
def create_connection():
    # Get the absolute path of the database file
    db_path = Path(__file__).resolve().parent.parent / 'database/retail_sales.db'
    print(f"Database absolute path: {db_path}") 
    
    try:
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        return conn
    except sqlite3.OperationalError as e:
        print(f"Error connecting to database: {e}")
        return None

# Home route
@app.route('/')
def index():
    return render_template('index.html')

# Data route to show records with optional search
@app.route('/data', methods=['GET', 'POST'])
def show_data():
    conn = create_connection()
    if conn is None:
        return "Database connection failed", 500

    cursor = conn.cursor()
    
    # Get the search query from the form (if any)
    search_query = request.args.get('search_query')
    
    # If there's a search query, filter the records
    if search_query:
        cursor.execute("""
            SELECT * FROM retail_sales 
            WHERE InvoiceNo LIKE ? OR StockCode LIKE ? OR Description LIKE ? OR Country LIKE ?
        """, ('%' + search_query + '%', '%' + search_query + '%', '%' + search_query + '%', '%' + search_query + '%'))
    else:
        # Otherwise, show all records
        cursor.execute("SELECT * FROM retail_sales LIMIT 100000")  # Adjust limit as needed
    
    rows = cursor.fetchall()
    conn.close()
    return render_template('data.html', rows=rows, search_query=search_query)


# Add new data form
@app.route('/add_data')
def add_data():
    return render_template('add_data.html', success=False, latest=None)

# Add new data to the database
@app.route('/add', methods=['POST'])
def add_record():
    if request.method == 'POST':
        # Get data from the form
        InvoiceNo = request.form['InvoiceNo']
        StockCode = request.form['StockCode']
        Description = request.form['Description']
        Quantity = request.form['Quantity']
        InvoiceDate = request.form['InvoiceDate']
        UnitPrice = request.form['UnitPrice']
        CustomerID = request.form['CustomerID']
        Country = request.form['Country']

        # Connect to the database
        conn = create_connection()
        if conn is None:
            return "Database connection failed", 500
        
        cursor = conn.cursor()

        # Insert data into the database
        cursor.execute('''
            INSERT INTO retail_sales (InvoiceNo, StockCode, Description, Quantity, InvoiceDate, UnitPrice, CustomerID, Country)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (InvoiceNo, StockCode, Description, Quantity, InvoiceDate, UnitPrice, CustomerID, Country))

        conn.commit()

        # Fetch the latest record just inserted
        cursor.execute("SELECT * FROM retail_sales ORDER BY rowid DESC LIMIT 1")
        latest = cursor.fetchone()

        conn.close()

        # Return to the form page with success message and latest entry
        return render_template('add_data.html', success=True, latest=latest)

# About page
@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)