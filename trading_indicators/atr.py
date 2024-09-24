import numpy as np
import pandas as pd
from .rma import rma

def atr(high: pd.Series, low: pd.Series, close: pd.Series, period=14):
  tr = np.maximum(high - low, np.abs(high - close.shift(1)), np.abs(low - close.shift(1)))
  atr_calc = rma(tr, period)
  return atr_calc
