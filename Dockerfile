FROM python:3.12-slim-bullseye
ENV DEBIAN_FRONTEND=noninteractive PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    libjpeg62-turbo \
  && rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

RUN useradd -m myuser && mkdir logs qr_codes && chown myuser:myuser logs qr_codes
COPY --chown=myuser:myuser . .
USER myuser

ENTRYPOINT ["python", "main.py"]
CMD ["--url", "http://github.com/kaw393939"]
