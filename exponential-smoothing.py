import pandas as pd
import matplotlib.pyplot as plt

def exponential_smoothing(alpha, data):
    smoothed_data = [data[0]]
    for i in range(1, len(data)):
        smoothed = alpha * data[i] + (1 - alpha) * smoothed_data[-1]
        smoothed_data.append(smoothed)
    return smoothed_data

def main():
    df = pd.read_csv("BBNI.JK.csv")
    
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)


    data_opening = df['Open'].tolist()
    data_closing = df['Close'].tolist()
    
    alpha = 0.3

    smoothed_data_opening = exponential_smoothing(alpha, data_opening)
    print(len(data_opening))
    smoothed_data_closing = exponential_smoothing(alpha, data_closing)

    #show forecasting of opening stock data
    forecasted_opening_24march2024 = alpha * data_opening[-1] + (1 - alpha)* smoothed_data_opening[-1]
    print("Forecasted opening of 24 March 2024: " + str(forecasted_opening_24march2024))

    plt.figure(figsize=(10, 6))
    plt.plot(df.index, data_opening, label='Opening Stock', color= 'blue')
    plt.plot(df.index, smoothed_data_opening, label='Opening Stock Forecast', color = 'red', linestyle='--')
    plt.plot(df.index[-1] + pd.DateOffset(days=1), forecasted_opening_24march2024, label = 'Opening Price Forecast for 24 March 2024', color= 'green', marker='o')
    plt.xlabel('Date')
    plt.ylabel('Price (IDR)')
    plt.title('Exponential Smoothing Forecasting of Opening Stock Prices')
    plt.legend()
    plt.grid(True)
    plt.show()

    #show forecasting of closing stock data
    forecasted_closing_24march2024 = alpha * data_closing[-1] + (1 - alpha)* smoothed_data_closing[-1]
    print("Forecasted closing of 24 March 2024: " + str(forecasted_closing_24march2024))
    plt.figure(figsize=(10, 6))
    plt.plot(df.index, data_closing, label='Closing Stock', color= 'blue')
    plt.plot(df.index, smoothed_data_closing, label='Closing Stock Forecasting', color = 'red', linestyle='--')
    plt.plot(df.index[-1] + pd.DateOffset(days=1), forecasted_closing_24march2024, label = 'Closing Price Forecast for 24 March 2024', color= 'green', marker='o')
    plt.xlabel('Date')
    plt.ylabel('Price (IDR)')
    plt.title('Exponential Smoothing Forecasting of Closing Stock Prices')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
