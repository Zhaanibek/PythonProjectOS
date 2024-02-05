# -*- coding: utf8 -*-

import os

from cryptography.fernet import Fernet


current = r'C:\Users\Qalam\PycharmProjects\pythonProject2\topic14_0_ProjectOS_FILE\data'
current_dir = os.listdir(current)

encrypted_reports = r'C:\Users\Qalam\PycharmProjects\pythonProject2\topic14_0_ProjectOS_FILE\encrypted_reports'
key_file_path = r'C:\Users\Qalam\PycharmProjects\pythonProject2\topic14_0_ProjectOS_FILE\spy\spykey.env'

if not os.path.exists('encrypted_reports'):
    print('Такой папки не существует!')
    os.makedirs(encrypted_reports)

if not os.path.exists(key_file_path):
    secret_key = Fernet.generate_key()
    with open(key_file_path, 'wb') as key_file:
        key_file.write(secret_key)
else:
    with open(key_file_path, 'rb') as key_file:
        secret_key = key_file.read()

fernet_key = Fernet(secret_key)

for filename in current_dir:
    full_path = os.path.join(current, filename)
    try:
        if 'c' not in filename:

            with open(full_path, 'rb') as file:
                read_data = file.read()

            encrypted_data = fernet_key.encrypt(read_data)
            join_path = os.path.join(encrypted_reports, filename)
            with open(join_path, 'wb') as joined_file:
                joined_file.write(encrypted_data)
            print(encrypted_data)
    except Exception as e:
        print(f'Ошибка при обработке файла {filename}: {e}')
