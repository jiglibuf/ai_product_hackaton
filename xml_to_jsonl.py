import pandas as pd
import json

def xlsx_to_jsonl(input_file, output_file):
    # Чтение Excel файла
    xls = pd.ExcelFile(input_file)
    sheets = xls.sheet_names
    
    # Список для хранения JSON Lines
    json_lines = []
    
    for sheet in sheets:
        # Чтение данных с текущего листа
        df = pd.read_excel(input_file, sheet_name=sheet)
        
        # Формирование JSON Lines
        for _, row in df.iterrows():
            json_obj = {
                "text": row['Название товара']
            }
            # Добавление меток классов для каждого листа
            for s in sheets:
                json_obj[s] = 1 if s == sheet else 0
            json_lines.append(json_obj)
    
    # Запись в JSON Lines файл
    with open(output_file, 'w', encoding='utf-8') as f:
        for line in json_lines:
            f.write(json.dumps(line, ensure_ascii=False) + '\n')

# Пример использования функции
input_file = 'dataset_LM_освещение.xlsx'  # Замените на ваше имя файла
output_file = 'output.jsonl'
xlsx_to_jsonl(input_file, output_file)
