#!/bin/sh

# Указание путей
JSON_FILE="../ex00/hh.json"  # Путь к JSON-файлу в папке ex00
OUTPUT_CSV="./hh.csv"       # CSV-файл, который будет создан в папке ex01
FILTER_FILE="./filter.jq"   # Фильтр jq в той же папке, что и скрипт

# Проверяем, существует ли JSON-файл
if [ ! -f "$JSON_FILE" ]; then
  echo "Ошибка: JSON-файл $JSON_FILE не найден!"
  exit 1
fi

# Проверяем, существует ли фильтр jq
if [ ! -f "$FILTER_FILE" ]; then
  echo "Ошибка: Фильтр jq $FILTER_FILE не найден!"
  exit 1
fi

# Добавляем заголовки в CSV-файл
echo "id,created_at,name,has_test,alternate_url" > $OUTPUT_CSV

# Применяем фильтр jq и записываем в CSV
jq -f "$FILTER_FILE" "$JSON_FILE" >> "$OUTPUT_CSV"

echo "Конвертация завершена. CSV-файл сохранён в $OUTPUT_CSV"
