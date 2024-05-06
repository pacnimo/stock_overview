# Stock Overview with BUY / HOLD / SELL Indicator

## Description
This application provides a streamlined interface for users to view and analyze stock recommendations. It categorizes stocks into different lists such as Top 100, Top US, Top DE, Top NL, and Top by Market Cap. For each stock, the application displays whether the stock is a buy, hold, or sell recommendation, along with its current price.

## How It Works
- **Data Fetching**: The application uses the `yfinance` library to fetch real-time data about various stocks from Yahoo Finance.
- **User Interaction**: Users can select different stock lists from a dropdown menu. Each selection triggers the app to fetch data corresponding to that specific stock list.
- **Display**: Stocks are displayed in a grid layout where each card represents a stock. The cards are color-coded: green for 'buy', red for 'sell', and gray for 'hold'. Each card shows the stock symbol, its current price, and its name on hover.
- **Caching**: To enhance performance, stock data fetching is cached. This means once a list is loaded, it will load quicker on subsequent requests until the cache is cleared or expired.

## Installation
1. Clone the repository:
git clone https://github.com/pacnimo/stock_overview

2. Install the required packages:
pip install -r requirements.txt


## Running the Application
To run the app, navigate to the project directory in your terminal and run:

streamlit run app.py

This will start the Streamlit server and open the application in your default web browser.

## Dependencies
- Streamlit
- yfinance
- pandas

Ensure you have the above dependencies installed to run the application smoothly.
