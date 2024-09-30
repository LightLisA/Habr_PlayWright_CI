import sys

def replace_in_file(file_path, search_text, replace_text):
    with open(file_path, 'r') as file:
        content = file.read()

    new_content = content.replace(search_text, replace_text)

    with open(file_path, 'w') as file:
        file.write(new_content)

# Отримуємо шлях до файлу як аргумент
path_to_file = sys.argv[1]

replace_in_file(path_to_file, 'from qaseio.model', 'from qaseio.models')
