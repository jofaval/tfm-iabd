# https://docs.docker.com/engine/reference/builder/
# Official doc: https://fastapi.tiangolo.com/deployment/docker/

FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt
COPY ./dev-requirements.txt /code/dev-requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/dev-requirements.txt

EXPOSE 80:80

COPY ./app /code/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]

# If running behind a proxy like Nginx or Traefik add --proxy-headers
# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80", "--proxy-headers"]