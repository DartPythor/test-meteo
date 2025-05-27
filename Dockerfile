FROM python:3.11-slim-bookworm

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libsqlite3-dev \
    git \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Копируем зависимости
COPY requirements/prod.txt .

# Устанавливаем зависимости
RUN pip install -U pip && \
    pip install -r prod.txt

# Копируем весь проект
COPY . .

# Изменяем рабочую директорию
WORKDIR /app/meteo

CMD ["sh", "-c", "python manage.py collectstatic --noinput && python manage.py migrate && gunicorn --bind 0.0.0.0:8000 meteo.wsgi"]