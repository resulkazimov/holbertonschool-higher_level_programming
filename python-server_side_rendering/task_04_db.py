import json
import csv
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

def read_json(filename):
    with open(filename, 'r') as f:
        return json.load(f)

def read_csv(filename):
    products = []
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
    return products

def read_sql(product_id=None):
    products = []
    try:
        conn = sqlite3.connect('products.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        if product_id:
            cursor.execute('SELECT name, category, price FROM Products WHERE id = ?', (product_id,))
        else:
            cursor.execute('SELECT name, category, price FROM Products')
        rows = cursor.fetchall()
        for row in rows:
            products.append(dict(row))
        conn.close()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    return products

@app.route('/products')
def display_products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    products = []
    error = None

    if source == 'json':
        products = read_json('products.json')
    elif source == 'csv':
        products = read_csv('products.csv')
    elif source == 'sql':
        products = read_sql() if not product_id else read_sql(int(product_id))
        if product_id and not products:
            return render_template('product_display.html', error="Product not found")
        return render_template('product_display.html', products=products)
    else:
        return render_template('product_display.html', error="Wrong source")

    # JSON və CSV üçün filterləmə (SQL artıq özü filterləyir)
    if product_id:
        product_id = int(product_id)
        products = [p for p in products if p['id'] == product_id]
        if not products:
            return render_template('product_display.html', error="Product not found")

    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
