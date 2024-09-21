import csv
from datetime import datetime, timedelta
import random
import string

# Параметры генерации данных
num_days = 30
num_users = 100
actions = ["CREATE", "READ", "UPDATE", "DELETE"]


# Функция для генерации случайного email
def generate_email():
    letters = string.ascii_lowercase
    username = ''.join(random.choice(letters) for i in range(random.randint(5, 10)))
    domain = ''.join(random.choice(letters) for i in range(random.randint(3, 7))) + '.com'
    return f"{username}@{domain}"


# Функция для генерации CSV-файлов
def generate_csv_files():
    start_date = datetime.now().date() - timedelta(days=num_days-1)
    for i in range(num_days):
        current_date = start_date + timedelta(days=i)
        filename = f"input/{current_date.strftime('%Y-%m-%d')}.csv"
        with open(filename, "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["email", "action", "dt"])
            for _ in range(random.randint(100, 1000)):
                email = generate_email()
                action = random.choice(actions)
                writer.writerow([email, action, current_date.strftime("%Y-%m-%d")])


generate_csv_files()
