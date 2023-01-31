# Data manipulation
# ==============================================================================

import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

# Scraper is initialized, symbol, start and end of download are included
# scraper = CmcScraper('BTC', '28-04-2013', '01-01-2022')

# Transform collected data into a dataframe
# btc = scraper.get_dataframe()

# btc.to_csv("btc.csv")

btc = pd.read_csv("btc.csv")

btc.sort_values(by=["Date"])

btc.index = pd.to_datetime(btc['Date'], format='%Y-%m-%d')

import matplotlib.pyplot as plt

train = btc[btc.index < pd.to_datetime("2020-11-01", format='%Y-%m-%d')]
test = btc[btc.index > pd.to_datetime("2020-11-01", format='%Y-%m-%d')]

# plt.plot(train, color = "black")
# plt.plot(test, color = "red")
# plt.ylabel('BTC Price')
# plt.xlabel('Date')
# plt.xticks(rotation=45)
# plt.title("Train/Test split for BTC Data")
# plt.show()


y = train['Open']

from statsmodels.tsa.arima.model import ARIMA

ARIMAmodel = ARIMA(y, order=(5, 4, 2))
ARIMAmodel = ARIMAmodel.fit()

y_pred = ARIMAmodel.get_forecast(len(test.index))
print("test.index")
print(test.index, len(test.index))
y_pred_df = y_pred.conf_int(alpha=0.05)
print("y_pred")
print(y_pred)
print("y_pred_df")
print(y_pred_df)
print(y_pred_df.index[0], y_pred_df.index[-1])
y_pred_df["Predictions"] = ARIMAmodel.predict(start=y_pred_df.index[0], end=y_pred_df.index[-1])
y_pred_df.index = test.index
y_pred_out = y_pred_df["Predictions"]
plt.plot(y_pred_out, color='Yellow', label='ARIMA Predictions')
plt.legend()
plt.show()

print("forecast")
print(ARIMAmodel.forecast(5))

import numpy as np
from sklearn.metrics import mean_squared_error

arma_rmse = np.sqrt(mean_squared_error(test["Open"].values, y_pred_df["Predictions"]))
print("RMSE: ", arma_rmse)
print(train[-6:])