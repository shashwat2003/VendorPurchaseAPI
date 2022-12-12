FROM python:3.11-alpine
RUN apk update && apk add gcc musl-dev mariadb-connector-c-dev git
WORKDIR /vendorPurchaseAPI
COPY requirements.txt /vendorPurchaseAPI
RUN pip3 install -r requirements.txt --no-cache-dir
RUN adduser --disabled-password --no-create-home django && \
    chown -R django:django /vendorPurchaseAPI && \
    chmod -R 755 /vendorPurchaseAPI
USER django