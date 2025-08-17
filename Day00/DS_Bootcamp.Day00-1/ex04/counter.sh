#!/bin/sh

# Указание путей
INPUT_FILE="../ex03/hh_positions.csv"     # Входной файл
OUTPUT_FILE="./hh_uniq_positions.csv" # Выходной файл

# Проверка наличия входного файла
if [ ! -f "$INPUT_FILE" ]; then
  echo "Ошибка: Входной файл $INPUT_FILE не найден!"
  exit 1
fi

# Обработка файла
{
  # Добавляем заголовок в выходной файл
  echo "\"name\",\"count\""
  
  # Извлекаем колонку position_level, подсчитываем уникальные значения и сортируем по убыванию
  tail -n +2 "$INPUT_FILE" | cut -d ',' -f 3 | sort | uniq -c | sort -nr | awk '{print "\"" $2 "\",\"" $1 "\""}'
} > "$OUTPUT_FILE"

echo "Подсчёт завершён. Результат сохранён в $OUTPUT_FILE"
