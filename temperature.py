
# Weekly Temperature Calculator
import sys

temps = [float(x) for x in sys.argv[1:8]]

if len(temps) != 7:
    print("Please enter exactly 7 temperatures")
    sys.exit(1)

average = sum(temps) / 7

print("Weekly Temperatures:", temps)
print("Average Temperature:", average)
