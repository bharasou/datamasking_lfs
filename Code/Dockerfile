FROM python:3.8

RUN pip install faker

COPY main.py csv_generator.py anonymize_csv.py /app/
COPY test_my_files.py /app/

WORKDIR /app

RUN python -m unittest test_my_files.py

CMD ["python", "main.py"]
