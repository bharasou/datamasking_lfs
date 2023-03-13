#importing packages and other python files to the main workspace
import csv
from Code.csv_generator import CSVGenerator
from Code.anonymize_csv import CSVAnonymizer

#assigning the original and anonymized data files to the local file
if __name__ == '__main__':
    input_filename = 'original_data.csv'
    output_filename = 'anonymized_data.csv'

    try:
        # Generating CSV file
        csv_generator = CSVGenerator(input_filename, 10)
        csv_generator.generate_csv()

        # AnonymizCSing V file
        csv_anonymizer = CSVAnonymizer(input_filename, output_filename)
        csv_anonymizer.anonymize_csv()

        # Printing the anonymized data
        # with open(output_filename, mode='r') as csvfile:
        #    reader = csv.DictReader(csvfile)
        #    for row in reader:
        #        print(row)
        
        with open(output_filename, mode='r') as input_file, open('output.csv', mode='w', newline='') as output_file:
            reader = csv.DictReader(input_file)
            writer = csv.DictWriter(output_file, fieldnames=reader.fieldnames)
            writer.writeheader()
            for row in reader:
                writer.writerow(row)

    #handling the exceptions
    except Exception as e:
        print(f"An error occurred: {str(e)}")
