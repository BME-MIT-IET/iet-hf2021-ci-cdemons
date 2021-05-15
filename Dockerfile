FROM python:3
WORKDIR /algorithms
COPY requirements.txt .
RUN pip3 install -r requirements.txt
RUN pip3 install algorithms
COPY . .
