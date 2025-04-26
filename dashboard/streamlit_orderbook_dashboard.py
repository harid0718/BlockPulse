import streamlit as st
import duckdb
import pandas as pd
from streamlit_autorefresh import st_autorefresh

# DuckDB path
duckdb_path = 'storage/blockpulse.duckdb'

# Streamlit page setup
st.set_page_config(page_title="BlockPulse Dashboard", layout="wide")
st.title("🚀 BlockPulse: Live Crypto Orderbook Aggregates")
st.caption("Real-time aggregation of buy/sell volumes from live order book streaming data")

# Auto-refresh every 5 seconds
st_autorefresh(interval=5000, key="dashboard_refresh")  # 5000 milliseconds = 5 seconds

def load_data():
    con = duckdb.connect(duckdb_path, read_only=True)
    query = """
        SELECT symbol, side, SUM(quantity) AS total_quantity
        FROM orderbook_aggregates
        GROUP BY symbol, side
        ORDER BY symbol, side
    """
    df = con.execute(query).fetchdf()
    con.close()
    return df

# Main page contents
df = load_data()

col1, col2 = st.columns(2)

with col1:
    st.subheader("Buy Volume per Symbol")
    buy_df = df[df['side'] == 'buy']
    st.bar_chart(data=buy_df, x='symbol', y='total_quantity')

with col2:
    st.subheader("Sell Volume per Symbol")
    sell_df = df[df['side'] == 'sell']
    st.bar_chart(data=sell_df, x='symbol', y='total_quantity')
