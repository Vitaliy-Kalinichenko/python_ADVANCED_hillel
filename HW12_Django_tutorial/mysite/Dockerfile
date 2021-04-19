
# Вытаскиваем базовый образ
FROM python:3.7-slim

# Устанавливаем переменные среды
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Настраиваем рабочий каталог
WORKDIR /mysite

COPY ./requirements.txt /mysite/
RUN pip install -r requirements.txt

# Копируем проект
COPY . /mysite/
