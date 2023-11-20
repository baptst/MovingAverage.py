import yfinance as yf
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg') 

start_date = '2020-01-01'
end_date = '2023-01-01'

symbol = 'AAPL'
data = yf.download(symbol, start=start_date, end=end_date)

print(data)

data['MA_50'] = data['Close'].rolling(window=50).mean()
data['MA_100'] = data['Close'].rolling(window=100).mean()
data['MA_200'] = data['Close'].rolling(window=200).mean()

plt.style.use("dark_background")
plt.figure(figsize=(12, 6))
plt.plot(data['Close'], label='Price')
plt.plot(data['MA_50'], label='50-day MA', color="orange")
plt.plot(data['MA_100'], label='100-day MA', color="green")
plt.plot(data['MA_200'], label='200-day MA', color="red")
plt.title(f'{symbol} Stock Price and Moving Averages Over the Last 3 Years')
plt.xlabel('Date')
plt.ylabel('Stock Price (USD)')
plt.legend()
plt.savefig('graph.png')
plt.show()



