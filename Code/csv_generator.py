#importing necessary packages for generating the CSV file
import csv
import random
import faker

#initiating a class for CSV generation
class CSVGenerator:
    def __init__(self, filename, num_rows):
        self.filename = filename
        self.num_rows = num_rows

    # Using faker package to generate realistic data
    def generate_csv(self):
        fake = faker.Faker()

        # Generating data for each row
        data = []
        for i in range(self.num_rows):
            row = {
                'first_name': fake.first_name(),
                'last_name': fake.last_name(),
                'address': fake.address(),
                'date_of_birth': fake.date_of_birth(minimum_age=18, maximum_age=80).strftime('%Y-%m-%d')
            }
            data.append(row)

        # Writing data to CSV file
        with open(self.filename, mode='w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=data[0].keys())
            writer.writeheader()
            for row in data:
                writer.writerow(row)
