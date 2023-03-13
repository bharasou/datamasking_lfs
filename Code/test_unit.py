import unittest
import os
from anonymize_csv import CSVAnonymizer
from csv_generator import CSVGenerator

class TestAnonymization(unittest.TestCase):
    def setUp(self):
        self.input_filename = 'original_data.csv'
        self.output_filename = 'anonymized_data.csv'
        self.num_rows = 10
        
    def test_csv_generator(self):
        filename = 'test.csv'
        num_rows = 5
        csv_generator = CSVGenerator(filename, num_rows)
        csv_generator.generate_csv()
        self.assertTrue(os.path.exists(filename))
        os.remove(filename)

    def test_csv_anonymizer(self):
        input_file = 'test.csv'
        output_file = 'test_anonymized.csv'
        with open(input_file, 'w') as f:
            f.write('first_name,last_name,address\n')
            f.write('John,Doe,123 Main St\n')
            f.write('Jane,Doe,456 High St\n')
        csv_anonymizer = CSVAnonymizer(input_file, output_file)
        csv_anonymizer.anonymize_csv()
        with open(output_file, 'r') as f:
            self.assertEqual(f.readline(), 'first_name,last_name,address\n')
            self.assertTrue(len(f.readline()) > 1)
            self.assertTrue(len(f.readline()) > 1)
        os.remove(input_file)
        os.remove(output_file)

    def test_main(self):
        os.system('python main.py')
        self.assertTrue(os.path.exists(self.output_filename))
        os.remove(self.input_filename)
        os.remove(self.output_filename)

if __name__ == '__main__':
    unittest.main()
