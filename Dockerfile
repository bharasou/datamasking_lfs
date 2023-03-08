FROM python:3.11

ADD Datamasking_modular.py .

RUN pip install Faker

CMD ["python", "./datamasking_modular.py"]