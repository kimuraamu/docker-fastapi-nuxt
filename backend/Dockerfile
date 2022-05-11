FROM python:3.7
ENV PYTHONUNBUFFERED 1
ENV LANG C.UTF-8
ENV TZ Asia/Tokyo
ENV APP_ROOT /code
WORKDIR ${APP_ROOT}
COPY . ${APP_ROOT}
RUN pip install -r requirements.txt
WORKDIR /code/app
CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]

