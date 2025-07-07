# se inicia construccion
FROM python:3.9-alpine as builder

WORKDIR /app

# se instala las dependencias de compilacion
RUN apk add --no-cache \
    gcc \
    musl-dev \
    libffi-dev

# se crea entorno virtual
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# se copia el requirements e instalar
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# copiamos  codigo fuente
COPY app.py .

# se crea la imagen minima
FROM alpine:3.18

# instalamos python
RUN apk add --no-cache python3

# entorno virtual
COPY --from=builder /opt/venv /opt/venv
COPY --from=builder /app/app.py /app/

# crear usuario
RUN addgroup -g 1000 appuser && \
    adduser -D -s /bin/sh -u 1000 -G appuser appuser

# configurar entorno
ENV PATH="/opt/venv/bin:$PATH"
WORKDIR /app

USER appuser

EXPOSE 8000

CMD ["python", "/opt/venv/bin/gunicorn", "--bind", "0.0.0.0:8000", "--workers", "1", "app:app"]
