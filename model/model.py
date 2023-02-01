import os

import numpy as np  # linear algebra
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
import tensorflow as tf
from matplotlib import pyplot as plt

from coin_thirdparty_tool import get_last_days_exchange

HORIZON = 2
WINDOW_SIZE = 3


def compute_dataframe(filename):
    df = pd.read_csv(f'data/{filename}.csv')
    df.drop(columns=['SNo', 'Name', 'Symbol', 'Open', 'Close', 'Volume', 'Marketcap', "Low"], axis=1, errors='ignore',
            inplace=True)
    # df['Date'] = df["Date"].dt.strftime('%y-%m-%d')
    df['Date'] = pd.to_datetime(df["Date"], format='%Y-%m-%d')
    df['Date'] = df['Date'].dt.strftime('%Y-%m-%d')
    df['Date'] = df['Date'].astype('datetime64[ns]')
    df.set_index("Date", inplace=True)

    return df


def plot_time_series(timesteps, values, coin, format='.', start=0, end=None, label=None):
    """
    Plots a timesteps (a series of points in time) against values (a series of values across timesteps).

    Parameters
    ---------
    timesteps : array of timesteps
    values : array of values across time
    format : style of plot, default "."
    start : where to start the plot (setting a value will index from start of timesteps & values)
    end : where to end the plot (setting a value will index from end of timesteps & values)
    label : label to show on plot of values
    """
    # Plot the series
    plt.plot(timesteps[start:end], values[start:end], format, label=label)
    plt.xlabel("Time")
    plt.ylabel(f"{coin} Price")
    if label:
        plt.legend(fontsize=14)  # make label bigger
    plt.grid(True)


def plot(dataframe, coin):
    prices = dataframe["High"].to_numpy()
    steps = tf.convert_to_tensor(dataframe.index.values.astype(np.int64))

    split_size = int(0.85 * len(prices))  # 80% train, 20% test

    # Create train data splits (everything before the split)
    x_train, y_train = steps[:split_size], prices[:split_size]

    # Create test data splits (everything after the split)
    x_test, y_test = steps[split_size:], prices[split_size:]
    len(x_train), len(x_test), len(y_train), len(y_test)
    plot_time_series(x_train, y_train, coin)
    plot_time_series(x_test, y_test, coin)
    plt.show()


def make_predictions(model, input_data):
    """
    Uses model to make predictions on input_data.

    Parameters
    ----------
    model: trained model
    input_data: windowed input data (same kind of data model was trained on)

    Returns model predictions on input_data.
    """
    forecast = model.predict(input_data)
    return tf.squeeze(forecast)


def get_labelled_windows(x, horizon=1):
    return x[:, :-horizon], x[:, -horizon:]


def make_windows(x, window_size=7, horizon=1):
    window_step = np.expand_dims(np.arange(window_size + horizon), axis=0)
    window_indexes = window_step + np.expand_dims(np.arange(len(x) - (window_size + horizon - 1)), axis=0).T
    windowed_array = x[window_indexes]
    windows, labels = get_labelled_windows(windowed_array, horizon=horizon)
    return windows, labels


def split_train_test(windows, labels):
    split_windows = int(0.85 * len(windows))
    split_labels = int(0.85 * len(labels))  # 80% train, 20% test
    # Create train data splits (everything before the split)
    x_train, x_test = windows[:split_windows], windows[split_windows:]

    # Create test data splits (everything after the split)
    y_train, y_test = labels[:split_labels], labels[split_labels:]

    return x_train, x_test, y_train, y_test


def train(coin):
    dataframe = compute_dataframe(coin)
    plot(dataframe, coin)
    prices = dataframe["High"].to_numpy()
    full_windows, full_labels = make_windows(prices, window_size=WINDOW_SIZE, horizon=HORIZON)
    train_windows, test_windows, train_labels, test_labels = split_train_test(full_windows, full_labels)

    model_7 = tf.keras.Sequential([
        tf.keras.layers.Lambda(lambda x: tf.expand_dims(x, axis=1)),
        tf.keras.layers.Conv1D(filters=128, kernel_size=5, padding="causal", activation='relu'),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dense(HORIZON, activation='linear'),
    ])
    model_7.compile(loss='mae',
                    optimizer='adam')
    history_model_7 = model_7.fit(x=train_windows, y=train_labels, batch_size=50, epochs=25, verbose=1,
                                  validation_data=(test_windows, test_labels))
    model_7.summary()
    model_7.save(coin)


def predict_for_model(model, values):
    cwd = os.getcwd()
    loaded = tf.keras.models.load_model(os.path.join(cwd, "model", model))
    custom = np.array(values)
    custom_window, custom_labels = make_windows(custom, window_size=WINDOW_SIZE, horizon=HORIZON)
    return make_predictions(loaded, custom_window)


def compute_percentage(coin):
    results = get_last_days_exchange(coin, 5)
    if results == -1 or results == -2:
        return results
    percentage = []
    values = []
    for price in results['prices']:
        values.append(price['usd'])
    result = predict_for_model('ETH-USD', values).numpy()
    percentage.append(result[0] / result[1] - 1)
    result = predict_for_model('DOGE-USD', values).numpy()
    percentage.append(result[0] / result[1] - 1)
    result = predict_for_model('BTC-USD', values).numpy()
    percentage.append(result[0] / result[1] - 1)
    return sum(percentage) / len(percentage) * 1000
