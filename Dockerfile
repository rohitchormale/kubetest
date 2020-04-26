FROM python:3.7.4-alpine3.10
LABEL name="kubetest"
ENV PYTHONBUFFERED 1
RUN mkdir -p /kubetest
COPY . /kubetest
WORKDIR /kubetest
RUN apk update
RUN python -m pip install --no-cache-dir -r requirements.txt
RUN python manage.py makemigrations \
    && python manage.py migrate
EXPOSE 8000
ENTRYPOINT [ "python", "manage.py" ]
CMD [ "runserver", "0.0.0.0:8000"]