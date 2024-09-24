import pandas as pd
import numpy as np
from datetime import time
from .trading_hours import trading_hours, Sessions

def trading_sessions(gmt_time: pd.Series):
  # Define session times in local time
  # Asian session: 9:00 - 18:00 Tokyo time
  # European session: 8:00 - 17:00 London time
  # American session: 8:00 - 17:00 New York time
  trading_sessions = pd.Series(index=gmt_time.index, data='', dtype=str)

  asian_session = trading_hours(gmt_time, (Sessions(start=time(9, 0), end=time(18, 0), zone='Asia/Tokyo'),))
  european_session = trading_hours(gmt_time, (Sessions(start=time(8, 0), end=time(17, 0), zone='Europe/London'),))
  american_session = trading_hours(gmt_time, (Sessions(start=time(8, 0), end=time(17, 0), zone='US/Eastern'),))

  # Assign sessions
  trading_sessions[asian_session] += 'asia '
  trading_sessions[european_session] += 'europe '
  trading_sessions[american_session] += 'america '

  # Clean up the results
  trading_sessions = trading_sessions.str.strip()
  trading_sessions = trading_sessions.replace('', np.nan)
  
  # Replace multiple sessions with combined names
  trading_sessions = trading_sessions.replace({
    'asia europe': 'asia_europe',
    'europe america': 'europe_america',
    'asia europe america': 'asia_europe_america'
  })

  return trading_sessions.astype(str)
