def add_time(start, duration, starting_day=None):
  days_of_week = [
    'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday',
    'Sunday'
  ]

  start_time, period = start.split()
  start_hour, start_minute = map(int, start_time.split(':'))
  duration_hour, duration_minute = map(int, duration.split(':'))

  new_minute = start_minute + duration_minute
  new_hour = start_hour + duration_hour + new_minute // 60
  new_minute %= 60

  if period == 'PM':
    new_hour += 12

  days_later = new_hour // 24
  new_hour %= 24

  new_period = 'PM' if new_hour >= 12 else 'AM'
  if new_hour > 12:
    new_hour %= 12

  if new_hour == 0:
    new_hour = 12

  new_time = f"{new_hour}:{str(new_minute).rjust(2, '0')} {new_period}"

  if starting_day:
    starting_day = starting_day.lower().capitalize()
    day_index = (days_of_week.index(starting_day) + days_later) % 7
    new_day = days_of_week[day_index]
    new_time += f", {new_day}"

  if days_later == 1:
    new_time += " (next day)"
  elif days_later > 1:
    new_time += f" ({days_later} days later)"

  return new_time
