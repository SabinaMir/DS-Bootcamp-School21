#!/bin/sh

# Указание выходного файла
OUTPUT_FILE="./hh_positions_combined.csv"

# Удаляем файл, если он уже существует
[ -f "$OUTPUT_FILE" ] && rm "$OUTPUT_FILE"

# Добавляем заголовок в выходной файл
echo '"id","created_at","name","has_test","alternate_url"' > "$OUTPUT_FILE"

# Обрабатываем все CSV-файлы, созданные partitioner.sh
for file in ./*.csv; do
  # Пропускаем файл результата
  if [ "$file" = "$OUTPUT_FILE" ]; then
    continue
  fi
  
  # Пропускаем заголовок (первые строки) и добавляем данные в выходной файл
  tail -n +2 "$file" >> "$OUTPUT_FILE"
done

echo "Файлы успешно объединены в $OUTPUT_FILE."
