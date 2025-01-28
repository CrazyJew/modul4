from datetime import datetime


def f_load_notes_from_file(file_name):

    list_notes = []
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            content = file.read()
            entries = content.split(f'-------------------\n')# Разделяем заметки по разделителю
            for entry in entries:
                if entry.strip():
                    note = {}
                    for line in entry.split('\n'):
                        if line.strip() and ':' in line:
                            key, value = line.split(':', 1)
                            note[key.strip().capitalize()] = value.strip()
                    if 'created_date' in note:
                        note['created_date'] = datetime.strptime(note['created_date'], '%d-%m-%Y')
                    if 'issue_date' in note:
                        note['issue_date'] = datetime.strptime(note['issue_date'], '%d-%m-%Y')
                list_notes.append(note)
    except FileNotFoundError:
        print(f'Файл {file_name}, не найден. Он будет создан автомотически')
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write('') #Создаем пустой файл
    return  list_notes



notes_list = f_load_notes_from_file('Blocnot')
if not notes_list:
    print('Файл отсутствует или является пустым')
else:
    for note in notes_list:
        print(note)
