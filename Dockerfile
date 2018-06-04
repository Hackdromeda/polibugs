FROM python:3.6
WORKDIR /app
ADD . /app
RUN pip install --trusted-host pypi.python.org -r requirements.txt
EXPOSE 8080
EXPOSE 5000
CMD ["python", "application.py"]