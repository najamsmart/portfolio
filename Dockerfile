FROM python:3.9.7
ADD ./python-flask
WORKDIR /python-flask
RUN pip insall -r requirements.txt
CMD ["python", "./app.py" ]