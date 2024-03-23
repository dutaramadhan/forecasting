import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def estimate_coef(x, y):
  n = np.size(x)
 
  m_x = np.mean(x)
  m_y = np.mean(y)
 
  SS_xy = np.sum(y*x) - n*m_y*m_x
  SS_xx = np.sum(x*x) - n*m_x*m_x
 
  b_1 = SS_xy / SS_xx
  b_0 = m_y - b_1*m_x
 
  return (b_0, b_1)
def main():
    df = pd.read_csv("BBNI.JK.csv")
    
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)

    x = df['Open']
    y = df['Close']

    coefficients = estimate_coef(x, y)

    #forecasted independent variable(harga opening saham) untuk tanggal 24 Maret 2024 menggunakan mean
    forecasted_independent_variable = df['Open'].mean()
    forecasted_dependent_variable = coefficients[0] + coefficients[1] * forecasted_independent_variable

    plt.figure(figsize=(10, 6))
    plt.scatter(x, y, color = "blue", marker = "o", s=30, label = 'Data')
    plt.plot(x, coefficients[0] + coefficients[1] * x, color = 'green', label = 'Linear Regression Line')
    plt.scatter(forecasted_independent_variable, forecasted_dependent_variable, color = 'red', label = 'Closing Price Forecast for 24 March 2024')
    plt.xlabel('Opening Prices (IDR)')
    plt.ylabel('Closing Prices(IDR)')
    plt.title('Linear Regression Forecasting of Closing Stock Prices')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
