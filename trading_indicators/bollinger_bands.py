import numpy as np
import pandas as pd

def bollinger_bands(close: pd.Series, period=20, std_dev=2.0, basis: pd.Series = np.nan):
  if np.isnan(basis):
    basis = close.rolling(window=period).mean()

  std = close.rolling(window=period).std()

  bb_middle = basis.astype(float)
  bb_upper = (bb_middle + (std_dev * std)).astype(float)
  bb_lower = (bb_middle - (std_dev * std)).astype(float)

  return bb_upper, bb_middle, bb_lower
