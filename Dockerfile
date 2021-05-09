FROM python:3
WORKDIR /algorithms
RUN pip3 install algorithms
COPY . .
