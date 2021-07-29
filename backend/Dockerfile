ARG IMAGE=base
FROM python:3.9-alpine as base

ENV PYTHONUNBUFFERED 1
EXPOSE 8000 8000

# Add runtime dependencies
RUN apk add --no-cache libpq libxslt libjpeg zlib jpeg bash postgresql-client binutils

COPY requirements.txt .

RUN apk add --no-cache --virtual build-deps gcc musl-dev postgresql-dev libxslt-dev jpeg-dev libffi-dev git rust cargo \
	&& pip install --no-cache-dir pip-tools \
	&& pip-sync \
	&& apk --purge del build-deps

RUN rm -f requirements.txt

FROM $IMAGE as build

RUN mkdir /app
COPY . /app/
WORKDIR /app/
CMD ["gunicorn", "asgi:application", "-k", "uvicorn.workers.UvicornWorker"]
