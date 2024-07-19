import matplotlib.pyplot as plt

# Data
days = ['Thursday', 'Wednesday', 'Tuesday', 'Monday', 'Sunday', 'Saturday', 'Friday']
percentages = [13.0, 20.0, 9.0, 20.0, 11.0, 13.0, 14.0]

# Create a pie chart
plt.figure(figsize=(10, 7))
plt.pie(percentages, labels=days, autopct='%1.1f%%', startangle=140)
plt.title('Percentage of Emails Received by Day of the Week')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Show the plot
plt.show()
