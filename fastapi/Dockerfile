#зададим родительский образ
FROM python:3.11
#устанавливаем рабочую директорию
#WORKDIR /ge
# добавляем директорию для данных
#RUN mkdir -p ./gx/uncommitted/data_docs/local_site
#копируем нужные файлы
COPY requirements.txt requirements.txt
COPY main.py main.py
#COPY /dynamic_sql_queries ./dynamic_sql_queries
#COPY /gx/checkpoints ./gx/checkpoints
#COPY /gx/expectations ./gx/expectations
#COPY /gx/great_expectations.yml ./gx/great_expectations.yml
#установим зависимости из файла
RUN pip install -r requirements.txt
#выполним код при старте контейнера
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8085"]
