def hours_minutes(seconds):
  hours = seconds//3600
  minutes = (seconds - 3600*hours)//60
  return (hours,minutes)

# Invoke the function and pass any integer as its argument
print(hours_minutes(3900))
