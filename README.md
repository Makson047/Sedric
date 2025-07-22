# Compliance Detection Pipeline

Цей проєкт — гнучкий Python-пайплайн для виявлення порушень регуляторних вимог у фінтех- та трейдингових компаніях з використанням LLM (Anthropic Claude). Підтримує різні типи перевірок: скарги клієнтів, попередження про запис розмови, агресивний маркетинг.



## 📦 Структура проекту

project_root/
├── main.py
├── compliance_checks.py
├── api_utils.py
├── pdf_utils.py
├── csv_utils.py
├── file_utils.py
├── prompt_utils.py
├── prompts/
│ ├── complaint_handling.txt
│ ├── call_recording_disclosure.txt
│ └── aggressive_marketing.txt
├── data_files/
│ └── ... (вхідні дані)
├── requirements.txt
└── README.md


## ⚙️ Вимоги

- Python 3.8+
- [Anthropic API ключ](https://console.anthropic.com/)
- Бібліотеки:
    - anthropic
    - python-dotenv
    - PyPDF2
    - (та стандартні бібліотеки Python)

Встановити всі залежності:
pip install -r requirements.txt 


## 🚀 Як запустити

1. Додайте API-ключ у .env файл:
ANTHROPIC_API_KEY=sk-ant-...

2. Підготуйте папку з файлами для перевірки (див. приклади нижче).

3. Запуск скрипта (CLI):
Complaint Handling and Escalation
python main.py --case complaint --input_folder data_files\Transcriptions\Complaints

Call Recording Disclosure
python main.py --case recording --input_folder "data_files\Transcriptions\Mock Calling Disclosure"

Aggressive or Pressuring Selling Language (Marketing)
python main.py --case marketing --input_folder data_files\Marketing_Assets


## 📄 Опис кейсів
- complaint — Виявлення скарг клієнтів, які не були відмічені агентом.
- recording — Виявлення відсутності попередження про запис розмови у дзвінках.
- marketing — Виявлення агресивного або оманливого маркетингу у PDF-файлах вебсторінок/реклами.


## 📝 Приклади структури вхідних даних
- Для complaint/recording: .txt файли з транскрипцією дзвінків.
- Для marketing: .pdf файли з маркетинговими матеріалами.


## 📤 Результати
Зберігаються у відповідних CSV-файлах:
- complaint.csv
- recording.csv
- marketing.csv
Кожен рядок містить результат для одного файлу.


## 🧩 Розширюваність
Для додавання нових типів перевірок:
- Додайте новий промпт у prompts/.
- Додайте новий чекер у compliance_checks.py.
- Оновіть логіку у main.py, якщо треба.


## ❗ Поради
- Переконайтесь, що всі змінні оточення (особливо ANTHROPIC_API_KEY) задані.
- Для маркетингових PDF бажано перевіряти якість витягнутого тексту.
- Для тесту на великій кількості файлів — дотримуйтесь лімітів Anthropic API.


##  📞 Підтримка
Для питань щодо розробки, звертайтесь через Issues або напряму до автора проєкту.