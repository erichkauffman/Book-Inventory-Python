FROM python:3.6-alpine

COPY /src /app

COPY requirements.txt /app/.

WORKDIR /app

RUN pip install -r requirements.txt

RUN python -m pytest

EXPOSE 5000

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]