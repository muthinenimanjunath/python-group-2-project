from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Database connection
def create_connection():
    conn = sqlite3.connect('database/retail_sales.db')
    conn.row_factory = sqlite3.Row
    return conn

# Home route
@app.route('/')
def index():
    return render_template('index.html')

# Data route to show records with optional search
@app.route('/data', methods=['GET', 'POST'])
def show_data():
    conn = create_connection()
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
        InvoiceNo = request.form['InvoiceNo']
        StockCode = request.form['StockCode']
        Description = request.form['Description']
        Quantity = request.form['Quantity']
        InvoiceDate = request.form['InvoiceDate']
        UnitPrice = request.form['UnitPrice']
        CustomerID = request.form['CustomerID']
        Country = request.form['Country']

        conn = create_connection()
        cursor = conn.cursor()

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