# 🚀 BlockPulse — Live Crypto Orderbook Analyzer

**BlockPulse** is a real-time big data streaming project that simulates crypto exchange order book updates, processes the data in microbatches, stores it in DuckDB, and visualizes live market dynamics through a Streamlit dashboard.


## 🛠️ Tools & Technologies

[![Python](https://img.shields.io/badge/Python-3.12-blue)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-yellow)](https://pandas.pydata.org/)
[![DuckDB](https://img.shields.io/badge/DuckDB-Lightweight%20Database-brightgreen)](https://duckdb.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red)](https://streamlit.io/)
[![Big Data](https://img.shields.io/badge/Big%20Data-Streaming-lightgrey)]()

---

## 📊 Project Architecture

```text
[Fake Orderbook Stream (Python)] 
         ↓
[Microbatch Aggregator (Pandas)] 
         ↓
[DuckDB (Local Database)] 
         ↓
[Streamlit Dashboard (Real-Time Visualization)]

```

---

## 🧩 Key Features
- **Real-Time Streaming:** Simulates live Binance-like order book activity
- **Microbatch Processing:** Aggregates new bids/asks every few seconds
- **Big Data Storage:** Efficient DuckDB storage for analytics
- **Dynamic Dashboard:** Interactive charts for buy/sell volume monitoring
- **Lightweight:** Runs fully locally without expensive cloud resources

---

## 🛠️ Tech Stack
- **Python 3.12**
- **Pandas** — for data aggregation
- **DuckDB** — for lightweight big data storage
- **Streamlit** — for dashboard visualization

---

## 🚀 How to Run the Project

1. **Clone the repository:**
    ```bash
    git clone https://github.com/harid0718/BlockPulse.git
    cd BlockPulse
    ```

2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Fake Data Generator:**
    ```bash
    python data_streamer/fake_orderbook_streamer.py
    ```

4. **Run the Microbatch Processor:**
    ```bash
    python processing/microbatch_orderbook_processor_with_duckdb.py
    ```

5. **Launch the Streamlit Dashboard:**
    ```bash
    streamlit run dashboard/streamlit_orderbook_dashboard.py
    ```

---

## 📸 Dashboard Preview

*(You can upload a screenshot here later)*

![BlockPulse Dashboard Screenshot](dashboard_preview.png)

---

## ✨ Future Improvements
- Add Top Gainers/Top Sellers tracking
- Simulate more market volatility scenarios
- Migrate to cloud-native streaming (Kafka, AWS Kinesis)
- Add historical trend analysis

---

## 👨‍💻 Author

- **Hari Dave** — MS Data Science student @ University of Arizona
