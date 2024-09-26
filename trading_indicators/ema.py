import pandas as pd

def ema(series: pd.Series, period: int):
  if period < 1:
    raise ValueError('Period must be greater than 0')
  if period == 1:
    return series
  alpha = 2 / (period + 1)
  ema_calc = series.ewm(alpha=alpha, adjust=False, min_periods=period).mean()
  return ema_calc.astype(float)
