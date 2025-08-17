#!/bin/sh

# Указание путей
INPUT_FILE="../ex02/hh_sorted.csv"   # Входной файл из папки ex02
OUTPUT_FILE="./hh_positions.csv"    # Выходной файл в папке ex03

# Проверка наличия входного файла
if [ ! -f "$INPUT_FILE" ]; then
  echo "Ошибка: Входной файл $INPUT_FILE не найден!"
  exit 1
fi

# Обработка файла
{
  # Извлечение заголовка и замена названия колонки
  head -n 1 "$INPUT_FILE" | awk -F',' 'BEGIN {OFS=","} {$3="position_level"; print $0}'
  
  # Обработка строк данных
  tail -n +2 "$INPUT_FILE" | awk -F',' '
    BEGIN {OFS=","}
    {
      # Проверка на наличие ключевых слов
      position_level = "-";
      if ($3 ~ /Junior/) position_level = position_level == "-" ? "Junior" : position_level "/Junior";
      if ($3 ~ /Middle/) position_level = position_level == "-" ? "Middle" : position_level "/Middle";
      if ($3 ~ /Senior/) position_level = position_level == "-" ? "Senior" : position_level "/Senior";
      $3 = position_level; # Замена колонки name на position_level
      print $0;
    }'
} > "$OUTPUT_FILE"

echo "Очистка завершена. Результат сохранён в $OUTPUT_FILE"
