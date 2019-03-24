FROM python:3.7-alpine

COPY /src /app

COPY requirements.txt /app/.

WORKDIR /app

RUN apk update && \
	apk add --no-cache gcc musl-dev

RUN pip install -r requirements.txt

RUN python -m pytest

EXPOSE 5000

ENTRYPOINT [ "gunicorn", "--worker-class", "eventlet" ]

CMD [ "-b", "0.0.0.0:5000", "-w", "1", "app:app" ]
