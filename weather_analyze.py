import csv
import matplotlib.pyplot as plt

options = ["Windspeed", "Winddegrees", "Windgust", "Tempature", "Tempature Feels Like"]
options_time = ["Year", "Month", "Hour", "Second"]

# Ask the user to choose a column
print("Choose between the following options:")
for option in options:
    print(option)
action = input("Enter your choice: ")

print("Choose between which timeline should the data be presented in:")
for option in options_time:
    print(option)
action_time = input("Enter your choice: ")

# If it's a valid option
if action in options:
    values = []
    time_stamp = []

    # Read the CSV and collect data from the selected column
    with open('weather_data.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                value = float(row[action.lower()])  # Convert to float for plotting
                print(value)
                values.append(value)
                time = float(row[action_time.lower()])
                time_stamp.append(time)
                print(time)
            except (ValueError, KeyError):
                continue  # Skip rows with missing or non-numeric data

    # Plotting
    plt.figure(figsize=(10, 5))
    plt.plot(time_stamp, values, 'o')  # 'o' creates a dot for each value
    plt.title(f'Dot Plot of {action}')
    plt.xlabel(action_time)
    plt.ylabel(action)
    plt.grid(True)
    plt.show()
else:
    print("Invalid option selected.")
