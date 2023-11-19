from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt

# Your Alpha Vantage API key
API_KEY = 'N8IN2LVTV9ZJQ71V'

# Initialize TimeSeries with your API key
ts = TimeSeries(key=API_KEY, output_format='pandas')

# List of stock symbols
stocks = ['CVNA', 'UPST', 'AI', 'BYND', 'VFS', 'FSR', 'NKLA', 'LKNC', 'WRC', 'BBBY', 'AMC', 'GME']

def fetch_and_plot(symbol):
    # Fetch stock data
    data, meta_data = ts.get_daily(symbol=symbol, outputsize='full')

    # Plotting
    plt.figure(figsize=(10, 4))
    data['4. close'].plot()
    plt.title(f'Closing Price of {symbol}')
    plt.xlabel('Date')
    plt.ylabel('Closing Price')
    plt.show()

if __name__ == '__main__':
    # Fetch and plot data for each stock
    for stock in stocks:
        fetch_and_plot(stock)
