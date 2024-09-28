"""
Author: Gordon Ombaka
Date: 21st September 2024

When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart’s maximum rate.
"""

# Get input from the user

age = int(input("Please enter your age: "))

# Calculate results

max_rate = 220 - age

range1 = 0.65 * max_rate

range2 = 0.85 * max_rate

# Display the results

print(f"When you exercise to strengthen your heart, you should keep your heart rate between {range1:.0f} and {range2:.0f} beats per minute.")