# Price Tracker Website

A web application to track the prices of items across various online platforms. This project scrapes product prices and provides users with insights like price trends and notifications when prices drop.

## Features
- **Real-time Price Tracking**: Scrapes prices from e-commerce websites.
- **Historical Data**: Tracks price trends over time.
- **User Notifications**: Alerts users when prices drop below a threshold.
- **Interactive Dashboard**: View price trends in a user-friendly interface.

## Tech Stack
### Backend
- **Framework**: Flask / FastAPI
- **Web Scraping**: BeautifulSoup, Requests
- **Database**: SQLite or SQLAlchemy
- **Scheduling**: Schedule / APScheduler

### Frontend
- **Framework**: React / Vanilla JavaScript
- **Styling**: Bootstrap / TailwindCSS
- **Charts**: Chart.js

## Installation
### Backend
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/price-tracker.git
   cd price-tracker/backend

2. Install dependencies:
    ```bash
    pip install -r requirements.txt

3. Set up enviroment variables: Create a .env file with:
    ```bash
    DATABASE_URL=sqlite:///price_tracker.db
    SECRET_KEY=your_secret_key

4. Run the backend server:
    ```bash
    python app.py