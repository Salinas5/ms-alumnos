FROM python:3.12-slim

ENV FLASK_CONTEXT=production
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV VIRTUAL_ENV="/home/flaskapp/.venv"
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN useradd --create-home --home-dir /home/flaskapp flaskapp

RUN apt-get update && \
    apt-get install -y build-essential curl libpq-dev python3-dev && \
    apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false && \
    rm -rf /var/lib/apt/lists/*


WORKDIR /home/flaskapp



RUN curl -sSL https://astral.sh/uv/install.sh -o uv-installer.sh && \
    sh uv-installer.sh && \
    rm uv-installer.sh

COPY ./pyproject.toml ./uv.lock ./
RUN pip install --no-cache-dir uv
RUN uv sync

COPY ./app ./app
COPY ./wsgi.py .

RUN chown -R flaskapp:flaskapp /home/flaskapp


USER flaskapp

EXPOSE 5000
CMD ["granian", "--port", "5000", "--host", "0.0.0.0", "--http", "auto", "--workers", "4", "--blocking-threads", "4", "--backlog", "2048", "--interface", "wsgi","wsgi:app"]
