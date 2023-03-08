import csv
from faker import Faker

def generate_data(num_rows):
    fake = Faker()
    data = []
    for i in range(num_rows):
        row = {}
        row['first_name'] = fake.first_name()
        row['last_name'] = fake.last_name()
        row['address'] = fake.address()
        row['date_of_birth'] = fake.date_of_birth().strftime('%m/%d/%Y')
        data.append(row)

    return data

def write_csv(filename, data):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['first_name', 'last_name', 'address', 'date_of_birth']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)

def anonymize_data(filename, anonymized_filename):
    with open(filename, 'r') as csvfile:
        fieldnames = ['first_name', 'last_name', 'address', 'date_of_birth']
        reader = csv.DictReader(csvfile, fieldnames=fieldnames)
        data = []
        for row in reader:
            row['first_name'] = 'Anonymous'
            row['last_name'] = 'User'
            row['address'] = 'Unknown'
            data.append(row)

    write_csv(anonymized_filename, data)
    print(data)

# generate and write CSV file
data = generate_data(10)
write_csv('data.csv', data)

# anonymize data and print
anonymize_data('data.csv', 'anonymized_data.csv')
