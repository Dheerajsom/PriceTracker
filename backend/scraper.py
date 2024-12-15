import requests
from bs4 import BeautifulSoup

def scrape_product(url):
    try:
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        # Customize these selectors based on the target website
        product_name = soup.find("span", {"id": "productTitle"}).get_text(strip=True)
        price_element = soup.find("span", {"class": "a-price-whole"})
        price = float(price_element.get_text(strip=True).replace(",", ""))

        return {"name": product_name, "price": price}
    except Exception as e:
        print(f"Error scraping product: {e}")
        return None
