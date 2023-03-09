#importing the necessary packages
import csv
import hashlib

#defining a class to anonymize
class CSVAnonymizer:
    def __init__(self, input_filename, output_filename):
        self.input_filename = input_filename
        self.output_filename = output_filename
    
    #opening both input CSV and output CSV files
    def anonymize_csv(self):
        with open(self.input_filename, mode='r') as input_file, \
                open(self.output_filename, mode='w', newline='') as output_file:
            reader = csv.DictReader(input_file)
            writer = csv.DictWriter(output_file, fieldnames=reader.fieldnames)
            writer.writeheader()

            # Passing  through each row in the input file and anonymizing the particular columns using md5 hasing
            for row in reader:
                try:
                    # Anonymizing first name
                    first_name_hash = hashlib.md5(row['first_name'].encode()).hexdigest()
                    row['first_name'] = first_name_hash
                    
                    # Anonymizing last name
                    last_name_hash = hashlib.md5(row['last_name'].encode()).hexdigest()
                    row['last_name'] = last_name_hash
                    
                    # Anonymizing address
                    address_hash = hashlib.md5(row['address'].encode()).hexdigest()
                    row['address'] = address_hash

                    # Writing anonymized row to output file
                    writer.writerow(row)
                except KeyError:
                    print(f"Error: CSV file missing required column(s)")
                    return
                except Exception as e:
                    print(f"Error: {str(e)}")
                    return
