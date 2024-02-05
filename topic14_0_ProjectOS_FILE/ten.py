
import os
import datetime

current = r'C:\Users\Qalam\PycharmProjects\pythonProject2\topic14_0_ProjectOS_FILE\data'
print(current)
current_dir = os.listdir(current)
#print(current_dir)
for filename in current_dir:
    w = datetime.datetime.strptime(filename[0:10], "%d_%M_%Y")
    d = datetime.datetime.strftime(w, "%d-%M-%Y")
    for october in range(31):
        if int(october + 1) == int(datetime.datetime.strftime(w, "%d")):
            print(f"{(october + 1)} == {int(datetime.datetime.strftime(w, "%d"))}")
