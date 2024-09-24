from datetime import time
import pandas as pd
import pytz

class Sessions:
  start: time
  end: time
  zone: str
  def __init__(self, start: time, end: time, zone: str) -> None:
    self.start = start
    self.end = end
    self.zone = zone

def trading_hours(gmt_time: pd.Series, session_filters: tuple[Sessions, ...]):
  gmt_time = gmt_time.copy().dt.tz_localize(pytz.UTC)
  trading_hours = pd.Series(index=gmt_time.index, data=False, dtype=bool)

  timezones = {session.zone: pytz.timezone(session.zone) for session in session_filters}
  times = {session.zone: gmt_time.dt.tz_convert(timezones[session.zone]) for session in session_filters}

  for session in session_filters:
    session_hours = (times[session.zone].dt.time >= session.start) & (times[session.zone].dt.time < session.end)
    trading_hours |= session_hours

  return trading_hours.astype(bool)
