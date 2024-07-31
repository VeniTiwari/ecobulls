import streamlit as st
import pandas as pd

# Set page configuration
st.set_page_config(page_title="Stocks News Segment", page_icon="📰")

# Header and description
st.markdown("# Stocks News Segment")
st.sidebar.header("Stocks News")

st.write(
    """This segment provides the latest headlines and stock price visualizations.
    (For demonstration purposes, stock price data is randomly generated.)"""
)

# Simulated news segments
st.subheader("📰 Today's Headline: Major Market Moves")
st.write("""
The stock market experienced significant volatility today as investors reacted to new economic data and corporate earnings reports. 
Major indices fluctuated throughout the day, reflecting the uncertainty and varied reactions from market participants.
""")

st.subheader("🔔 Stock Market LIVE Updates: Sensex up 200 pts, Nifty above 24,900; Asian Paints, NTPC lead gains")
st.write("""
**Sensex Today | Stock Market LIVE Updates:** NTPC, Asian Paints, BPCL, Tata Motors and Adani Enterprises are among the top gainers on the Nifty, while losers are Divis Labs, Tata Consumer, Tata Motors, Axis Bank and Power Grid Corp.
""")

# Market indices data
market_data = pd.DataFrame({
    'Index': ['Sensex', 'Nifty 50', 'Nifty Bank'],
    'Prices': [81681.39, 24935.25, 51481.50],
    'Change': [225.99, 77.95, -17.80],
    'Change%': [0.28, 0.31, -0.03]
})
st.table(market_data)

# Biggest Gainers and Losers
st.subheader("📈 Biggest Gainer & Loser")
gainers_data = pd.DataFrame({
    'Company': ['Asian Paints', 'Divis Labs'],
    'Prices': [3088.00, 4845.60],
    'Change': [82.95, -66.75],
    'Change%': [2.76, -1.36]
})
st.table(gainers_data)

# Sector performance
st.subheader("📊 Sector Performance")
sector_data = pd.DataFrame({
    'Sector': ['Nifty Pharma', 'Nifty PSU Bank'],
    'Prices': [21745.00, 7400.30],
    'Change': [204.20, -28.25],
    'Change%': [0.95, -0.38]
})
st.table(sector_data)

# Stock price table
st.subheader("📈 Stock Prices")
stock_price_data = pd.DataFrame({
    'STOCKS': ['TCS', 'HDFC Bank', 'ICICI Bank'],
    'CURRENT PRICE': [4380, 1608.15, 1217.3],
    'DAY\'S HIGH': [4431.25, 1631.7, 1242.45]
})
st.table(stock_price_data)

# Additional news segments
st.subheader("🏦 RBI Update")
st.write("""
**Reserve Bank of India to hold rates in August, first cut in Q4**: A sharp spike in food prices drove inflation in Asia's third-largest economy to a five-month high of 5.08% in June, well above the RBI's 4% medium-term target, suggesting the central bank will be wary of easing monetary policy too soon.
""")

st.subheader("💼 Company News")
st.write("""
**Dixon to start making Google Pixel from September, Atul Lall confirms CCI nod for Transsion deal**: Leading electronics manufacturer Dixon Technologies has secured the Competition Commission of India's clearance to acquire a majority 50.10 per cent share in Ismartu India - a subsidiary of Chinese handset maker Transsion Technology.
""")

st.subheader("📈 Midcap Index Performance")
midcap_data = pd.DataFrame({
    'Company': ['Torrent Power', 'Linde India', 'Persistent'],
    'CMP': [1873.65, 8344.55, 4958.15],
    'Chg%': [17.13, 4.31, 3.73],
    'Volume': [267.09, 9.34, 20.59]
})
st.table(midcap_data)

# Footer
st.write("---")
st.write("Data and content are for demonstration purposes only. Not actual financial advice.")
