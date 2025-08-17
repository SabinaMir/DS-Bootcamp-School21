#!/bin/bash

# Название файла для сохранения данных
OUTPUT_FILE="hh.json"

# Выполнение запроса curl и форматирование JSON с помощью jq
curl -s "https://api.hh.ru/vacancies?text=data%20scientist&per_page=20&page=0" | jq '.' > $OUTPUT_FILE

# Проверка, успешно ли выполнен запрос
if [ $? -eq 0 ]; then
  echo "Данные о вакансиях успешно сохранены и отформатированы в $OUTPUT_FILE."
else
  echo "Произошла ошибка при загрузке данных."
  exit 1
fi
