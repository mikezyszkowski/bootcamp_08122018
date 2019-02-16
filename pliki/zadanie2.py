#program sumujący z pliku czas zalogowania dla unikalnych użytkowników

import sys
from collections import defaultdict

try:
    f_name = sys.argv[1]
except IndexError:
    print("Nie podałeś nazwy pliku")
    exit()


def prepare_line(text):
    login, action, time = text.split(";")
    time = int(time)
    return login, action, time


def my_key(login):
    return int(login[0].split("-")[-1])


last_login_time = {}
user_total_time = defaultdict(int)


try:
    with open(f_name) as f:
        for line in f:
            login, action, time = prepare_line(line)
            if action == "LOGIN":
                last_login_time[login] = time
            elif action == "LOGOUT":
                session_time = time - last_login_time[login]
                user_total_time[login] += session_time
    for login, time in sorted(user_total_time.items(), key=my_key):
        print(f"{login} : {time}s")

except FileNotFoundError:
    print("Nie ma takiego pliku")

print("-"*40)
print(last_login_time)
print(user_total_time)
