import pandas as pd
import os
import sys
from datetime import datetime, timedelta


def load_logs(start_date, end_date):
    logs = []

    # Обход всех дней от start_date до end_date
    current_date = start_date
    while current_date <= end_date:
        file_name = f'input/{current_date.strftime("%Y-%m-%d")}.csv'
        if os.path.exists(file_name):
            daily_logs = pd.read_csv(file_name)
            logs.append(daily_logs)
        current_date += timedelta(days=1)

    # Объединение всех загруженных логов
    if logs:
        return pd.concat(logs, ignore_index=True)
    else:
        return pd.DataFrame(columns=['email', 'action', 'dt'])


def aggregate_actions(logs):
    # Сгруппируем данные по email и action, подсчитав количество действий
    action_counts = logs.groupby(['email', 'action']).size().unstack(fill_value=0)

    # Переименуем колонки
    action_counts.columns = [f"{action.lower()}_count" for action in action_counts.columns]

    return action_counts.reset_index()


def save_to_csv(aggregated_data, output_date):
    output_dir = 'output'
    os.makedirs(output_dir, exist_ok=True)

    output_file = os.path.join(output_dir, f'{output_date}.csv')
    aggregated_data.to_csv(output_file, index=False)


def main(date_str):
    date = datetime.strptime(date_str, '%Y-%m-%d')
    start_date = date - timedelta(days=7)
    end_date = date - timedelta(days=1)

    logs = load_logs(start_date, end_date)

    if logs.empty:
        print("No logs found for the specified date range.")
        return

    aggregated_data = aggregate_actions(logs)

    save_to_csv(aggregated_data, date_str)
    print(f'Aggregated data saved to {date_str}.csv in the output directory.')


main('2024-09-21')
print()
