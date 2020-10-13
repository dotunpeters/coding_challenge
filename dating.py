from datetime import datetime, date, time, timedelta
from pytz import UTC

print(datetime.now(tz=UTC).microsecond)
print(date.today())

#timedelta operation
print(datetime.now() + timedelta(weeks=7))
print((date.today() - date(1995, 2, 13)).days)
print((date.today() - date(1995, 2, 13)).total_seconds())