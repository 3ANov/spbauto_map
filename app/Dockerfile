# pull official base image
FROM python:3.8.6-alpine

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk add --no-cache \
            --upgrade \
        postgresql-client \
        libpq \
    && apk add --no-cache \
               --upgrade \
               --virtual .build-deps \
        postgresql-dev \
        zlib-dev jpeg-dev \
        alpine-sdk \
    && apk add --no-cache \
               --upgrade \
        geos \
        proj \
        gdal \
        binutils \
    && ln -s /usr/lib/libproj.so.15 /usr/lib/libproj.so \
    && ln -s /usr/lib/libgdal.so.20 /usr/lib/libgdal.so \
    && ln -s /usr/lib/libgeos_c.so.1 /usr/lib/libgeos_c.so \
    && apk add --no-cache libffi-dev openssl-dev cargo

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt
RUN pip install git+https://github.com/location-iq/locationiq-python-client.git

# copy entrypoint.sh
COPY ./entrypoint.sh .

# copy project
COPY . .

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]