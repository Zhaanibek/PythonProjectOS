# -*- coding: cp1251 -*-

from dotenv import load_dotenv
import os
import datetime

current = r'C:\Users\Qalam\PycharmProjects\pythonProject2\topic14_0_ProjectOS_FILE\data'
print(current)
current_dir = os.listdir(current)
#print(current_dir)
day = 0

    #print(f"d = {d}")


#for october in range(31):
#    print(october + 1)

with open(r'data\01_10_2023_cachalot.txt', 'r') as file1:
    read1 = file1.read()

with open(r'data\03_10_2023_whale.txt', 'r') as file2:
    read2 = file2.read()

with open(r'data\06_10_2023_cheetah.txt', 'r') as file3:
    read3 = file3.read()

with open(r'data\07_10_2023_gorilla.txt', 'r') as file4:
    read4 = file4.read()

with open(r'data\10_10_2023_dolphin.txt', 'r') as file5:
    read5 = file5.read()

with open(r'data\13_10_2023_tiger.txt', 'r') as file6:
    read6 = file6.read()

with open(r'data\18_10_2023_elephant.txt', 'r') as file7:
    read7 = file7.read()

with open(r'data\19_10_2023_giraffe.txt', 'r') as file8:
    read8 = file8.read()

with open(r'data\21_10_2023_penguin.txt', 'r') as file9:
    read9 = file9.read()

with open(r'data\28_10_2023_koala.txt', 'r') as file10:
    read10 = file10.read()

with open(r'spy\spy.key', 'r') as secret_key:
    read_secret_key1 = secret_key.read()

fernet_key1 = Fernet(read_secret_key1)
decrypted_data1 = fernet_key1.decrypt(read1)

fernet_key2 = Fernet(read_secret_key1)
decrypted_data2 = fernet_key2.decrypt(read2)

fernet_key3 = Fernet(read_secret_key1)
decrypted_data3 = fernet_key3.decrypt(read3)

fernet_key4 = Fernet(read_secret_key1)
decrypted_data4 = fernet_key4.decrypt(read4)

fernet_key5 = Fernet(read_secret_key1)
decrypted_data5 = fernet_key5.decrypt(read5)

fernet_key6 = Fernet(read_secret_key1)
decrypted_data6 = fernet_key6.decrypt(read6)

fernet_key7 = Fernet(read_secret_key1)
decrypted_data7 = fernet_key7.decrypt(read7)

fernet_key8 = Fernet(read_secret_key1)
decrypted_data8 = fernet_key8.decrypt(read8)

fernet_key9 = Fernet(read_secret_key1)
decrypted_data9 = fernet_key9.decrypt(read9)

fernet_key10 = Fernet(read_secret_key1)
decrypted_data10 = fernet_key10.decrypt(read10)

for day in range(1, 32):
    find = False
    for filename in current_dir:
        w = datetime.datetime.strptime(filename[0:10], "%d_%m_%Y")
        d = w.day
        if day == int(d):
            print(f"Отчет за {day} октября: {(decrypted_data1.decode('utf-8'))}")
            find = True
            break
    if not find:
        print(f"За {day} октября отчетов нет.")

print(decrypted_data1.decode('utf-8'))
print(decrypted_data2.decode('utf-8'))
print(decrypted_data3.decode('utf-8'))
print(decrypted_data4.decode('utf-8'))
print(decrypted_data5.decode('utf-8'))
print(decrypted_data6.decode('utf-8'))
print(decrypted_data7.decode('utf-8'))
print(decrypted_data8.decode('utf-8'))
print(decrypted_data9.decode('utf-8'))
print(decrypted_data10.decode('utf-8'))

