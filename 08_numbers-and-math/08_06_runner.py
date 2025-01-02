# If a runner runs 10 miles in 30 minutes and 30 seconds,
# What is their average speed in kilometers per hour?
# (Tip: 1 mile = 1.6 km)

# Define variable
distance_miles = 10
time_minutes = 30
time_seconds = 30

# Convert distance to kilometers
distance_km = distance_miles * 1.6

# Convert total time to hours
total_minutes = time_minutes + (time_seconds / 60.0)
time_hours = total_minutes / 60.0

# Calculate speed in km/h
average_speed_kph = distance_km / time_hours

print("Average Speed:", average_speed_kph, "km/h")
