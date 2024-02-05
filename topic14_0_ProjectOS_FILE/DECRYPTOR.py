# -*- coding: utf8 -*-

import os
import datetime

from cryptography.fernet import Fernet

current = r'C:\Users\Qalam\PycharmProjects\pythonProject2\topic14_0_ProjectOS_FILE\data'
current_dir = os.listdir(current)

for day in range(1, 32):
    find = False
    for filename in current_dir:
        full_path = os.path.join(current, filename)
        try:
            with open(full_path, 'rb') as file:
                read_data = file.read()
            with open(r'spy\spy.key', 'rb') as secret_key:
                read_secret_key = secret_key.read()

            fernet_key = Fernet(read_secret_key)
            decrypted_data = fernet_key.decrypt(read_data)
            w = datetime.datetime.strptime(filename[0:10], "%d_%m_%Y")
            d = w.day
            if day == int(d):
                find = True
                join_path = os.path.join('decrypted_reports', filename)
                with open(join_path, 'w') as joined_file:
                    joined_file.write(decrypted_data.decode('utf-8').lower())
                break

        except Exception as e:
            print(f'Ошибка: {e}')

    if not find:
        print(f"За {day} октября отчетов нет.")

# remove_dir = os.listdir(
#    r'C:\Users\Qalam\PycharmProjects\pythonProject2\topic14_0_ProjectOS_FILE\decrypted_reports')
# for file in remove_dir:
# file_path = os.path.join(r'decrypted_reports', file)
# os.remove(file_path)
