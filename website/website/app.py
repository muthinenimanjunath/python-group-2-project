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

# Data route to show records
@app.route('/data')
def show_data():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM retail_sales")  # Adjust limit as needed
    rows = cursor.fetchall()
    conn.close()
    return render_template('data.html', rows=rows)

# Add new data form
@app.route('/add_data')
def add_data():
    return render_template('add_data.html')

# Add new data to the database
@app.route('/add', methods=['POST'])
def add_record():
    if request.method == 'POST':
        InvoiceNo = request.form['InvoiceNo'] #Text
        StockCode = request.form['StockCode'] #Text
        Description = request.form['Description'] #Text
        Quantity = request.form['Quantity'] #Integer
        InvoiceDate = request.form['InvoiceDate'] #Text (datetime string) YYYY-MM-DD HH:MM:SS
        UnitPrice = request.form['UnitPrice'] #Real (float)
        CustomerID = request.form['CustomerID'] #Integer
        Country = request.form['Country'] #Integer (encoded as category)
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO retail_sales (InvoiceNo, StockCode, Description, Quantity, InvoiceDate, UnitPrice, CustomerID, Country)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', 
            (InvoiceNo, StockCode, Description, Quantity, InvoiceDate, UnitPrice, CustomerID, Country))
        conn.commit()
        conn.close()
        return redirect(url_for('show_data'))
# About page
@app.route('/about')
def about():
    return render_template('about.html')
if __name__ == '__main__':
    app.run(debug=True)