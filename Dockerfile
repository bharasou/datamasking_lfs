FROM python:3.8

ADD DataMasking.py .
ADD Unittest.py .


CMD [ "python3", "./DataMasking.py" , "Unittest.py"]
