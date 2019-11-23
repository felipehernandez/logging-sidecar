FROM python:3.7-alpine
LABEL app="logging-sidecar"

COPY requirements.txt /
RUN pip install --upgrade setuptools
RUN pip install -r /requirements.txt

COPY src/ /src
COPY app.py .

EXPOSE 5001

CMD ["python", "-u", "app.py"]