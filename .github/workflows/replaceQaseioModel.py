import os

def replace_in_file(file_path, search_text, replace_text):
    with open(file_path, 'r') as file:
        content = file.read()

    new_content = content.replace(search_text, replace_text)

    with open(file_path, 'w') as file:
        file.write(new_content)

# Знаходимо файл у вашій віртуальній машині
path_to_file = 'path_to_your_virtualenv/site-packages/qaseio/commons/testops.py'

replace_in_file(path_to_file, 'from qaseio.model', 'from qaseio.models')
