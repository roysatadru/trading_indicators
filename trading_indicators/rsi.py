import pandas as pd
import pandas_ta as ta

def rsi(close: pd.Series, period: int):
  rsi_calc = ta.rsi(close, period)
  return rsi_calc.astype(float)
