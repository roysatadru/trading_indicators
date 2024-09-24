import pandas as pd
import pandas_ta as ta

def vwap(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, datetime_index: pd.Series):
  original_index = high.index

  high = high.copy()
  low = low.copy()
  close = close.copy()
  volume = volume.copy()
  datetime_index = datetime_index.copy()

  high.index = datetime_index
  low.index = datetime_index
  close.index = datetime_index
  volume.index = datetime_index

  vwap_calc: pd.Series = ta.vwap(high, low, close, volume)
  vwap_calc.index = original_index
  return vwap_calc.astype(float)
