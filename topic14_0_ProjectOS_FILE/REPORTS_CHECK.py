# -*- coding: utf8 -*-

import os

current_replaced = r'C:\Users\Qalam\PycharmProjects\pythonProject2\topic14_0_ProjectOS_FILE\decrypted_reports'
current_replaced_dir = os.listdir(current_replaced)

print(f'Проверенные данные: ')
for changed_report in current_replaced_dir:
    full_path = os.path.join(current_replaced, changed_report)
    try:
        with open(full_path, 'r') as file:
            data = file.read()

        with open(full_path, 'w') as file:
            if 'вра' in data:
                changed_data = data.replace('вра', 'дру')
                file.write(changed_data)
                print(f'{changed_data} Проверено!')

    except Exception as e:
        print(f"Ошибка: {e}")
