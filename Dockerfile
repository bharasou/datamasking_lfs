FROM python:3.8

RUN pip install pandas faker

COPY main.py csv_generator.py anonymize_csv.py /app/

WORKDIR /app

CMD ["python", "main.py"]
