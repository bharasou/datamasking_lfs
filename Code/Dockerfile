FROM python:3.8

RUN pip install pandas faker

COPY main.py csv_generator.py anonymize_csv.py /app/
COPY test_unit.py /app/

WORKDIR /app

RUN python -m unittest test_unit.py

CMD ["python", "main.py"]
