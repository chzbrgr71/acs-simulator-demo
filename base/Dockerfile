FROM python:2.7.12

RUN pip install --upgrade pip

COPY requirements.txt requirements.txt

RUN pip install --pre azure
RUN pip install azure-storage >= 0.20.3
RUN pip install pydocumentdb
