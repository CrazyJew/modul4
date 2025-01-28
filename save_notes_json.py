import json

note = [
    {
        "username": "Алексей",
        "title": "Список покупок",
        "content": "Купить продукты",
        "status": "новая",
        "created_date": "27-11-2024",
        "issue_date": "30-11-2024"
    }
]


def f_saves_notes_json (note, file_name):
    try:
        with open(file_name, 'w', encoding='utf-8') as file:
            json.dump(note, file, ensure_ascii=False, indent=4)
            print('Файл успешно создан')
    except Exception as e:
        print(f"Произошла ошибка : {e}")


