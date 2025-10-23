FROM python:3.10-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN  apk update && apk add --no-cache \ 
gcc \ 
musl-dev \ 
mariadb-dev \ 
pkgconfig \ 
python3-dev \ 
libffi-dev \ 
openssl-dev \ 
&& rm -rf /var/cache/apk/*

RUN apk add --no-cache shadow

COPY requirements.txt /app/
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

RUN groupadd -r drfgroup && useradd -r -g drfgroup tomas

RUN mkdir -p /app/staticfiles
RUN chown -R tomas:drfgroup /app/staticfiles

USER tomas




COPY . /app/

EXPOSE 8000 

RUN python manage.py collectstatic --noinput

CMD ["gunicorn","--workers","2","project.wsgi:application","--bind","0.0.0.0:8000"]