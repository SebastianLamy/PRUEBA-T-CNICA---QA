FROM python:3.11-slim


WORKDIR /app


# instalar dependencias del sistema necesarias para playwright
RUN apt-get update && apt-get install -y curl gnupg libgtk-3-0 libxss1 libasound2 libnss3 libx11-6 libxkbfile1 libpangocairo-1.0-0 libatk1.0-0 libatk-bridge2.0-0 libgbm1 libxcomposite1 libxrandr2 libxdamage1 libxfixes3 libxrender1 ca-certificates && rm -rf /var/lib/apt/lists/*


COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


# instalar navegadores para playwright
RUN python -m playwright install --with-deps


COPY src/ ./src
COPY perf/ ./perf


CMD ["pytest", "--maxfail=1", "--disable-warnings", "-q", "src/api_tests/"]