FROM python:3.11.7-slim

COPY ./app/ /app/

WORKDIR /app

ENV PATH=/root/.local/bin:$PATH

RUN pip install --user dumb-init poetry \
    && poetry install

ENTRYPOINT [ "dumb-init", "--" ]
CMD ["sh", "-c", "poetry run gunicorn $APP_FILE_NAME:app --bind 0.0.0.0:80 --threads $NUM_OF_THREADS"]
