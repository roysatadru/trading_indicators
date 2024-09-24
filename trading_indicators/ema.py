import pandas as pd

def ema(series: pd.Series, period: int):
  alpha = 2 / (period + 1)
  ema_calc = series.ewm(alpha=alpha, adjust=False, min_periods=period).mean()
  return ema_calc.astype(float)
