

note = {'username': 'Иван', 'title': 'План работы', 'content': 'Завершить проект', 'status': 'выполнено',
     'created_date': '20-11-2024', 'issue_date': '26-11-2024'}

def f_append_notes_to_file(note, fail_name):
    try:
        with open(fail_name, 'a', encoding='utf-8') as file:
            for key, value in note.items():
                file.write(f'{key}: {value}\n')
            file.write("-" * 20 + "\n")
            print('Заметка успешно добавлена')
    except Exception as i:
        print(f'Произошла ошибка при записи заметки: {i}')


f_append_notes_to_file(note, 'Blocnot.txt')