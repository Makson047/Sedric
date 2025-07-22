import csv
import os

def save_result_to_csv(result, csv_path):
    """
    Зберігає результат перевірки у CSV-файл.
    Якщо файл не існує — додає заголовок.
    """
    file_exists = os.path.isfile(csv_path)
    with open(csv_path, "a", newline='', encoding="utf-8") as csvfile:
        writer = csv.DictWriter(
            csvfile,
            fieldnames=list(result.keys())
        )
        if not file_exists:
            writer.writeheader()
        writer.writerow(result)