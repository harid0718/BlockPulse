import pandas as pd
import numpy as np
import time
import os
from datetime import datetime

# Config
BASE_PRICES = {
    "BTCUSDT": 65000,
    "ETHUSDT": 3500,
    "BNBUSDT": 550
}
TICK_SIZE = {
    "BTCUSDT": 5,
    "ETHUSDT": 1,
    "BNBUSDT": 0.5
}
ORDER_COUNT = (10, 50)  # min-max number of bids/asks per batch
QUANTITY_RANGE = (0.01, 2)  # min-max quantity per order
SLEEP_TIME = 0.5  # seconds between batches

# Make sure storage exists
os.makedirs('storage', exist_ok=True)
file_path = 'storage/live_orderbook.csv'

def generate_orders(symbol, base_price, tick_size):
    bids = []
    asks = []
    
    # Random number of bids and asks
    num_bids = np.random.randint(*ORDER_COUNT)
    num_asks = np.random.randint(*ORDER_COUNT)
    
    for _ in range(num_bids):
        price = base_price - np.random.uniform(0, tick_size*20)
        quantity = np.random.uniform(*QUANTITY_RANGE)
        bids.append((price, quantity))
        
    for _ in range(num_asks):
        price = base_price + np.random.uniform(0, tick_size*20)
        quantity = np.random.uniform(*QUANTITY_RANGE)
        asks.append((price, quantity))
        
    return bids, asks

def main():
    # If file doesn't exist, create it
    if not os.path.isfile(file_path):
        header = pd.DataFrame(columns=["symbol", "price", "quantity", "side", "timestamp"])
        header.to_csv(file_path, index=False)

    while True:
        all_orders = []
        
        for symbol, base_price in BASE_PRICES.items():
            # Simulate base price slight random walk
            new_base = base_price + np.random.uniform(-TICK_SIZE[symbol], TICK_SIZE[symbol])
            BASE_PRICES[symbol] = new_base  # update
            
            bids, asks = generate_orders(symbol, new_base, TICK_SIZE[symbol])
            
            bid_records = [(symbol, price, quantity, 'buy', datetime.now()) for price, quantity in bids]
            ask_records = [(symbol, price, quantity, 'sell', datetime.now()) for price, quantity in asks]
            
            all_orders.extend(bid_records + ask_records)
        
        # Save to CSV
        df = pd.DataFrame(all_orders, columns=["symbol", "price", "quantity", "side", "timestamp"])
        df.to_csv(file_path, mode='a', header=False, index=False)
        
        print(f"Saved {len(all_orders)} new orders at {datetime.now()}")
        
        time.sleep(SLEEP_TIME)

if __name__ == "__main__":
    main()
