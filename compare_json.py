import json
import os

# Путь к файлу en.json и ru.json
en_json_path = "en.json"
ru_json_path = "ru.json"

# Загрузка содержимого файлов
with open(en_json_path, "r", encoding="utf-8") as en_file:
    en_data = json.load(en_file)

with open(ru_json_path, "r", encoding="utf-8") as ru_file:
    ru_data = json.load(ru_file)

# Сравнение en.json и ru.json
en_keys = set(en_data.keys())
ru_keys = set(ru_data.keys())

# Если ключи в en.json изменились
if en_keys != ru_keys:
    ru_data = en_data
else:
    # Если ключи остались теми же, сравним значения
    for key in en_keys:
        if en_data[key] != ru_data[key]:
            ru_data[key] = en_data[key]

# Запись обновленных данных в ru.json
with open(ru_json_path, "w", encoding="utf-8") as ru_file:
    json.dump(ru_data, ru_file, indent=4, ensure_ascii=False)

# Удаление временных файлов
os.remove(en_json_path)
