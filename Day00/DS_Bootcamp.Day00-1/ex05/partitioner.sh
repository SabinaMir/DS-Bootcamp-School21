#!/bin/sh

# Указание пути к входному файлу
INPUT_FILE="../ex03/hh_positions.csv"

# Проверка наличия входного файла
if [ ! -f "$INPUT_FILE" ]; then
  echo "Ошибка: Входной файл $INPUT_FILE не найден!"
  exit 1
fi

# Пропускаем заголовок и обрабатываем строки
tail -n +2 "$INPUT_FILE" | while IFS=',' read -r id created_at name has_test alternate_url
do
  # Извлекаем дату из поля created_at (до символа T)
  date=$(echo "$created_at" | cut -d'T' -f1)
  
  # Создаём файл для этой даты, если его ещё нет, и добавляем заголовок
  if [ ! -f "./${date}.csv" ]; then
    echo '"id","created_at","name","has_test","alternate_url"' > "./${date}.csv"
  fi
  
  # Добавляем строку в соответствующий файл
  echo "$id,$created_at,$name,$has_test,$alternate_url" >> "./${date}.csv"
done

echo "Данные успешно разделены по датам."
