import sys

temps = [float(x) for x in sys.argv[1:8]]

if len(temps) != 7:
    print("Please enter exactly 7 temperatures")
    sys.exit(1)

average = sum(temps) / 7
highest = max(temps)
lowest = min(temps)

print("Weekly Temperatures:", temps)
print("Average Temperature:", average)
print("Highest Temperature:", highest)
print("Lowest Temperature:", lowest)