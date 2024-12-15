import sqlite3
from datetime import datetime

DB_NAME = "price_tracker.db"

def initialize_database():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Create tables
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            url TEXT NOT NULL,
            current_price REAL NOT NULL,
            price_threshold REAL NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS price_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_id INTEGER NOT NULL,
            price REAL NOT NULL,
            timestamp TEXT NOT NULL,
            FOREIGN KEY (product_id) REFERENCES products (id)
        )
    """)

    conn.commit()
    conn.close()

def add_product(name, url, current_price, price_threshold):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO products (name, url, current_price, price_threshold)
        VALUES (?, ?, ?, ?)
    """, (name, url, current_price, price_threshold))

    product_id = cursor.lastrowid

    cursor.execute("""
        INSERT INTO price_history (product_id, price, timestamp)
        VALUES (?, ?, ?)
    """, (product_id, current_price, datetime.now().isoformat()))

    conn.commit()
    conn.close()

    return product_id

def get_tracked_products():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, name, url, current_price, price_threshold
        FROM products
    """)
    products = cursor.fetchall()

    conn.close()
    return [{"id": row[0], "name": row[1], "url": row[2], "current_price": row[3], "price_threshold": row[4]} for row in products]

def get_price_history(product_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT price, timestamp
        FROM price_history
        WHERE product_id = ?
        ORDER BY timestamp ASC
    """, (product_id,))
    history = cursor.fetchall()

    conn.close()
    return {"prices": [row[0] for row in history], "dates": [row[1] for row in history]}