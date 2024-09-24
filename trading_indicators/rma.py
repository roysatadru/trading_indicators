import pandas as pd

def rma(series: pd.Series, period: int):
  alpha = 1 / period
  rma_calc = series.ewm(alpha=alpha, adjust=False, min_periods=period).mean()
  return rma_calc.astype(float)
