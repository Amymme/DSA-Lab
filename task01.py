# List of dictionaries of pre-defined rivers
rivers = [
    {"name": "Nile", "length": 4157},
    {"name": "Yangtze", "length": 3434},
    {"name": "Murray-Darling", "length": 2310},
    {"name": "Volga", "length": 2290},
    {"name": "Mississippi", "length": 2540},
    {"name": "Amazon", "length": 3915}
]

# Task 1.
# Display the name of each river
for river in rivers:
    print(river["name"])

# Task 2.
# Display the total length of the rivers
total = 0
for river in rivers:
    total += river["length"]
print(f"Total length is {total} miles")

# Task 3.
for river in rivers:
    # Only keep those names that start with "M"
    if river["name"].startswith("M"):
        print(river["name"])

# Task 4.
# Display the lengths in kilometres
for river in rivers:
    print(f"The length of {river['name']} is {river['length']*1.6:.2f} km")