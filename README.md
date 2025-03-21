# 🤖 CALORISCANBOT

![Python](https://img.shields.io/badge/Python-3.13.2-blue?logo=python&logoColor=white)
![aiogram](https://img.shields.io/badge/aiogram-latest-blue?logo=telegram&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-latest-orange?logo=postgresql&logoColor=white)
![asyncio](https://img.shields.io/badge/asyncio-built--in-green)
![License](https://img.shields.io/badge/License-Educational--Only-red)

**⚠️ EDUCATIONAL PURPOSES ONLY. NOT FOR PRODUCTION USE ⚠️**

## 📝 Description

CALORISCANBOT is a modern Telegram bot built with Python 3.13 that analyzes nutritional information. The bot uses asynchronous programming paradigms and leverages the latest Python features to provide a fast and responsive user experience.


## 🛠️ Technologies

- **Python 3.13.2**: Latest Python version with performance improvements
- **aiogram**: Modern framework for Telegram Bot API
- **SQLAlchemy**: SQL toolkit and ORM for database operations
- **asyncio**: Python's built-in asynchronous I/O framework
- **uv**: Fast Python package installer and resolver


## 🚀 Installation

### Prerequisites
- Python 3.13.2
- uv package manager

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/caloriscanbot.git
   cd caloriscanbot
   ```

2. Install dependencies using uv:
   ```bash
   curl -sSf https://astral.sh/uv/install.sh | sh
   uv pip install -e .
   ```

3. Configure environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

## 📋 Usage

Start the bot with:
```bash
uv run main.py
```

### Docker Deployment
```bash
docker build -t caloriscanbot .
docker run -d --name calorisbot caloriscanbot
```

## ⚠️ Disclaimer

This project is intended for **educational purposes only**. It demonstrates modern Python practices, asynchronous programming, and bot development techniques. Usage in production environments is strictly prohibited.

## 📜 License

This code is provided for educational purposes only and is not licensed for commercial or personal use.

Copyright © 2025
