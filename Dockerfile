FROM python:3.13.2-slim

WORKDIR /app

# Установка необходимых системных зависимостей
RUN apt-get update && apt-get install -y \
    curl \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Установка uv
RUN curl -sSf https://astral.sh/uv/install.sh | sh
ENV PATH="/root/.cargo/bin:${PATH}"

# Копирование файлов зависимостей
COPY pyproject.toml uv.lock ./

# Копирование файла .env для переменных окружения
COPY .env ./

# Установка зависимостей через uv
RUN uv pip install .

# Копирование кода проекта
COPY app/ ./app/
COPY database/ ./database/
COPY handlers/ ./handlers/
COPY middlewares/ ./middlewares/
COPY models.py requests.py config.py main.py ./

# Настройка переменных окружения
ENV PYTHONUNBUFFERED=1

# Запуск бота через uv
CMD ["uv", "run", "main.py"]