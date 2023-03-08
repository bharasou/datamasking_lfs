import csv
import random
import string

# Function to generate a random string of specified length
def random_string(length):
    return ''.join(random.choice(string.ascii_letters) for i in range(length))

# Generate a CSV file with random data
with open('data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['first_name', 'last_name', 'address', 'date_of_birth'])
    for i in range(10):
        writer.writerow([random_string(8), random_string(10), random_string(20), f"{random.randint(1,28)}/{random.randint(1,12)}/{random.randint(1950,2020)}"])

# Load the CSV file and anonymize first_name, last_name, and address fields
with open('data.csv', mode='r') as file:
    reader = csv.DictReader(file)
    anonymized_data = []
    for row in reader:
        anonymized_row = {'first_name': '****', 'last_name': '****', 'address': '****', 'date_of_birth': row['date_of_birth']}
        anonymized_data.append(anonymized_row)

# Output anonymized data to a different file
with open('anonymized_data.csv', mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['first_name', 'last_name', 'address', 'date_of_birth'])
    writer.writeheader()
    writer.writerows(anonymized_data)

# Print the anonymized data
with open('anonymized_data.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)