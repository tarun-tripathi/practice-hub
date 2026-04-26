# Q6: Stock Price Prediction using LSTM
# Task: Predict future stock prices using LSTM neural network
# Data source: Yahoo Finance via yfinance library
# Install: pip install yfinance tensorflow keras scikit-learn matplotlib
# Docs: https://keras.io/api/layers/recurrent_layers/lstm/

import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout

STOCK = "TCS.NS"
START = "2020-01-01"
END = "2024-01-01"
LOOKBACK = 60

# Download data
print(f"Downloading {STOCK} data...")
df = yf.download(STOCK, start=START, end=END)
data = df["Close"].values.reshape(-1, 1)

# Scale data
scaler = MinMaxScaler()
scaled = scaler.fit_transform(data)

# Create sequences
X, y = [], []
for i in range(LOOKBACK, len(scaled)):
    X.append(scaled[i - LOOKBACK:i, 0])
    y.append(scaled[i, 0])

X, y = np.array(X), np.array(y)
X = X.reshape(X.shape[0], X.shape[1], 1)

# Split
split = int(0.8 * len(X))
X_train, X_test = X[:split], X[split:]
y_train, y_test = y[:split], y[split:]

# Build LSTM model
model = Sequential([
    LSTM(50, return_sequences=True, input_shape=(LOOKBACK, 1)),
    Dropout(0.2),
    LSTM(50, return_sequences=False),
    Dropout(0.2),
    Dense(1)
])

model.compile(optimizer="adam", loss="mean_squared_error")
model.summary()

print("Training model...")
model.fit(X_train, y_train, epochs=10, batch_size=32, validation_split=0.1)

# Predict
predictions = scaler.inverse_transform(model.predict(X_test))
actual = scaler.inverse_transform(y_test.reshape(-1, 1))

# Plot
plt.figure(figsize=(12, 6))
plt.plot(actual, label="Actual Price")
plt.plot(predictions, label="Predicted Price")
plt.title(f"{STOCK} Stock Price Prediction (LSTM)")
plt.xlabel("Days")
plt.ylabel("Price (INR)")
plt.legend()
plt.savefig("stock_prediction.png")
print("Plot saved as stock_prediction.png")