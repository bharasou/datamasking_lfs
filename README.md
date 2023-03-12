# Data Engineering Coding Challenge for Latitude Financial Services
Thank you for giving me the opportunity to present my skills in this coding challenge. I have given my best approach towards solving this challenge and provide you the best practice on problem-solving, and I have structured my code in a comprehensible manner for review.

For this coding challenge I have chosen the Anonymize customer information problem. 

## Problem Statement - 1 (Anonymize customer information)
Imagine you are working on a project where you have to process customer data and generate insights. Considering this data has customer information and to generate insights, multiple teams will be using this data. To ensure we handle customer information with care, and not make it visible to everyone on the team one requirement is to anonymize customer information before it's loaded into the warehouse for insights generation.

- You will get this data in CSV files which will have customer personal information like first_name, last_name, address, date_of_birth
- Write code to generate a CSV file containing first_name, last_name, address, date_of_birth
- Load generated CSV in the previous step, anonymize data, and output anonymized data to a different file
- Columns to anonymise are first_name, last_name and address


## Data Masking Project
This project provides a data masking solution that anonymizes sensitive data in CSV files using various techniques.

### Prerequisites
1. Docker
2. Python 3.x

### The files that are available in the github repo are 
1. csv_generator.py
2. anonymize_csv.py
3. main.py
4. Unittest.py
5. Docker file

To see the output of the project, follow the below mentioned steps.

### Dockerfile
The Dockerfile for this project installs the necessary Python packages, copies the project files to the container, and sets the command to run the main.py script
In docker terminal, to build the docker image in your environment, run the following command

```
docker build -t data-masking .
```

Once the docker builds the image for the file, type the following command to run the application, run:

```
docker run data-masking
```

The masked data will be generated in the output directory with a csv file.

### Masking Techniques
The following masking techniques are supported:

md5 hashing: masks the column value using a secure one-way hash function
