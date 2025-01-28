

notes = [{'username': 'Алексей',
        'title': 'Список покупок',
        'content': 'Купить продукты на неделю',
        'status': 'новая',
        'created_date': '27-11-2024',
        'issue_date': '30-11-2024'},
        {'username': 'Мария',
         'title': 'Учеба',
         'content': 'Подготовиться к экзамену',
         'status': 'в процессе',
         'created_date': '25-11-2024',
         'issue_date': '01-12-2024'}]


def f_save_notes_to_file (notes, file_name):
    with open('Blocnot.txt', 'w', encoding= 'UTF-8') as file:
        for d in notes:
            for key, value in d.items():
                file.write(f'{key.capitalize()}: {value}\n')
            file.write("-" * 20 + "\n") #Разделяем заметки
f_save_notes_to_file(notes, 'Blocnot')