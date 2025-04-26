import pandas as pd
import duckdb
import time
import os

# Storage paths
file_path = 'storage/live_orderbook.csv'
duckdb_path = 'storage/blockpulse.duckdb'

# Wait until file exists
while not os.path.exists(file_path):
    print("Waiting for data...")
    time.sleep(2)

# Connect to DuckDB
con = duckdb.connect(database=duckdb_path, read_only=False)

# Create table if not exists
con.execute("""
CREATE TABLE IF NOT EXISTS orderbook_aggregates (
    batch_time TIMESTAMP,
    symbol VARCHAR,
    side VARCHAR,
    quantity DOUBLE
)
""")

print("Data file found and database ready! Starting microbatch processing...")

# Keep track of last processed row
last_row = 0

while True:
    try:
        # Read the growing CSV
        df = pd.read_csv(file_path)

        # Only process new rows
        if len(df) > last_row:
            new_df = df.iloc[last_row:]

            # Aggregation
            agg_df = new_df.groupby(['symbol', 'side'])['quantity'].sum().reset_index()
            agg_df['batch_time'] = pd.Timestamp.now()
            agg_df = agg_df[['batch_time', 'symbol', 'side', 'quantity']]

            # OPEN CONNECTION fresh
            con = duckdb.connect(database=duckdb_path, read_only=False)

            # Save to DuckDB
            agg_df.to_sql('orderbook_aggregates', con, if_exists='append', index=False)

            # CLOSE CONNECTION immediately
            con.close()

            print("\n--- New Microbatch Saved ---")
            print(agg_df)

            # Update last_row tracker
            last_row = len(df)

        time.sleep(5)

    except Exception as e:
        print(f"Error occurred: {e}")
        time.sleep(5)

