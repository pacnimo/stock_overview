import streamlit as st
import yfinance as yf
import pandas as pd
from top_100 import symbols as top_100_symbols
from top_us import symbols as top_us_symbols
from top_de import symbols as top_de_symbols
from top_nl import symbols as top_nl_symbols
from top_mc import symbols as top_mc_symbols

@st.cache_resource
def fetch_data(symbols):
    data = []
    for symbol in symbols:
        stock = yf.Ticker(symbol)
        info = stock.info
        recommendation = info.get('recommendationKey', 'none')
        price = info.get('currentPrice', 'N/A')
        long_name = info.get('longName', 'Unknown')
        data.append({'symbol': symbol, 'price': price, 'recommendation': recommendation, 'long_name': long_name})
    return pd.DataFrame(data)

# Set the page configuration with meta tags
st.set_page_config(
    page_title="Stock Overview",
    page_icon=":chart_with_upwards_trend:",
    layout="wide",
    menu_items={
        'Get Help': 'https://www.example.com/help',
        'Report a bug': "https://www.example.com/bug",
        'About': "### This is a Stock Overview App\nIt provides a simple interface to monitor stock BUY/SELL recommendations."
    }
)

# Main title and application information
st.title('Stock Overview with BUY / HOLD / SELL Indicator')
st.caption('This application provides an overview of stock recommendations based on different stock lists. Select a list to view the corresponding stocks and their recommendations. Explore more on our [GitHub](https://github.com/your-repo-here) or check out related projects: [Project1](https://example.com/project1), [Project2](https://example.com/project2).')


# Selector for different stock lists
option = st.selectbox(
    'Choose a stock list',
    ('Top 100', 'Top US', 'Top DE', 'Top NL', 'Top by Market Cap')
)

# Stock list options
if option == 'Top 100':
    stock_symbols = top_100_symbols
elif option == 'Top US':
     stock_symbols = top_us_symbols
elif option == 'Top DE':
     stock_symbols = top_de_symbols
elif option == 'Top NL':
     stock_symbols = top_nl_symbols
elif option == 'Top by Market Cap':
     stock_symbols = top_mc_symbols

data = fetch_data(stock_symbols)

# Display cards in a grid
col_count = 10
cols = st.columns(col_count)
index = 0
for _, row in data.iterrows():
    with cols[index % col_count]:
        color = 'green' if row['recommendation'] == 'buy' else 'red' if row['recommendation'] == 'sell' else 'gray'
        st.markdown(
            f"<div title='{row['long_name']}' style='background-color:{color};padding:10px;margin-bottom:5px;border-radius:10px;'>"
            f"<h3>{row['symbol']}</h3><h4>${row['price']}</h4></div>",
            unsafe_allow_html=True
        )
    index += 1

# Footer
st.markdown("---")
st.markdown("© 2024 Streamlit Stock Dashboard. All rights reserved.")

