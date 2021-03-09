FROM python:3

WORKDIR /usr/src/api-server

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY api_server.py ./

CMD ["python", "./api_server.py"]