from flask import Flask, request, jsonify
import scraper 
from database import (
    initialize_database,
    add_product,
    get_tracked_products,
    get_price_history,
)

app = Flask(__name__)

# Initialize the database
initialize_database()

@app.route("/add-product", methods=["POST"])
def add_product_endpoint():
    data = request.json
    product_url = data.get("url")
    price_threshold = data.get("threshold")

    # Scrape product details
    product = scraper.scrape_product(product_url)
    if not product:
        return jsonify({"error": "Failed to scrape product data"}), 400

    # Add product to the database
    product_id = add_product(product["name"], product_url, product["price"], price_threshold)
    return jsonify({"id": product_id, **product}), 201

@app.route("/tracked-products", methods=["GET"])
def get_tracked_products_endpoint():
    products = get_tracked_products()
    return jsonify(products), 200

@app.route("/price-history", methods=["GET"])
def get_price_history_endpoint():
    product_id = request.args.get("id")
    if not product_id:
        return jsonify({"error": "Product ID is required"}), 400

    history = get_price_history(product_id)
    return jsonify(history), 200

if __name__ == "__main__":
    app.run(debug=True)
