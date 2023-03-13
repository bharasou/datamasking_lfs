import unittest
import csv
import random
import string
import os

class TestAnonymizeCSV(unittest.TestCase):

    # Generate a CSV file with random data for testing
    @classmethod
    def setUpClass(cls):
        with open('test_data.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['first_name', 'last_name', 'address', 'date_of_birth'])
            for i in range(10):
                writer.writerow([random_string(8), random_string(10), random_string(20), f"{random.randint(1,28)}/{random.randint(1,12)}/{random.randint(1950,2020)}"])

    # Remove the generated test CSV file
    @classmethod
    def tearDownClass(cls):
        os.remove('test_data.csv')
        os.remove('anonymized_test_data.csv')

    # Function to generate a random string of specified length
    def random_string(self, length):
        return ''.join(random.choice(string.ascii_letters) for i in range(length))

    # Test that the anonymized CSV file is created successfully
    def test_anonymize_csv(self):
        # Load the test CSV file and anonymize it
        with open('original_data.csv', mode='r') as file:
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

        # Check that the anonymized CSV file was created successfully
        self.assertTrue(os.path.isfile('anonymized_test_data.csv'))

    # Test that the anonymized CSV file contains the correct data
    def test_anonymized_data(self):
        # Load the anonymized CSV file and check the anonymized data
        with open('anonymized_test_data.csv', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.assertEqual(row['first_name'], '****')
                self.assertEqual(row['last_name'], '****')
                self.assertEqual(row['address'], '****')
                self.assertTrue(row['date_of_birth'].count('/') == 2)