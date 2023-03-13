import unittest
import os
from csv_generator import CSVGenerator
from anonymize_csv import CSVAnonymizer

class TestCSV(unittest.TestCase):
    def setUp(self):
        self.input_filename = 'original_data.csv'
        self.output_filename = 'anonymized_data.csv'
        self.num_rows = 10
        
        # generate test data
        csv_generator = CSVGenerator(self.input_filename, self.num_rows)
        csv_generator.generate_csv()
        
        # anonymize test data
        csv_anonymizer = CSVAnonymizer(self.input_filename, self.output_filename)
        csv_anonymizer.anonymize_csv()

    def tearDown(self):
        os.remove(self.input_filename)
        os.remove(self.output_filename)

    def test_file_exists(self):
        self.assertTrue(os.path.isfile(self.input_filename))
        self.assertTrue(os.path.isfile(self.output_filename))

    def test_file_size(self):
        self.setUp()  # call setUp() before running the test
        self.assertGreater(os.path.getsize(self.input_filename), 0)
        self.assertGreater(os.path.getsize(self.output_filename), 0)

    def test_anonymization(self):
        self.setUp()  # call setUp() before running the test
        with open(self.input_filename) as f1, open(self.output_filename) as f2:
            for line2, line3 in zip(f1, f2):
                # check that first name is anonymized
                self.assertNotEqual(line2.split(',')[0], line3.split(',')[0])
                # check that last name is anonymized
                self.assertNotEqual(line2.split(',')[1], line3.split(',')[1])
                # check that address is anonymized
                self.assertNotEqual(line2.split(',')[2], line3.split(',')[2])

if __name__ == '__main__':
    unittest.main()
