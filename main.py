import argparse
import os
import glob
from compliance_checks import check_complaint_handling, check_call_recording_disclosure, check_aggressive_marketing
from pdf_utils import extract_text_from_pdf
from csv_utils import save_result_to_csv
from file_utils import load_transcription


"""
Приклади запуску:
    python main.py --case complaint --input_folder data_files\Transcriptions\Complaints
    python main.py --case recording --input_folder "data_files\Transcriptions\Mock Calling Disclosure"
    python main.py --case marketing --input_folder data_files\Marketing_Assets
"""


def parse_args():
    parser = argparse.ArgumentParser(description="Compliance batch checker")
    parser.add_argument("--case", required=True, choices=["complaint", "recording", "marketing"],
                        help="Який кейс перевіряємо: complaint | recording | marketing")
    parser.add_argument("--input_folder", required=True,
                        help="Папка з файлами для перевірки")
    return parser.parse_args()


def get_checker(case):
    if case == "complaint":
        return check_complaint_handling
    elif case == "recording":
        return check_call_recording_disclosure
    elif case == "marketing":
        return check_aggressive_marketing
    else:
        raise ValueError("Unknown case!")


if __name__ == "__main__":
    args = parse_args()
    checker = get_checker(args.case)
    output_csv = f"{args.case}.csv"

    if args.case == "marketing":
        files = glob.glob(os.path.join(args.input_folder, "*.pdf"))
    else:
        files = glob.glob(os.path.join(args.input_folder, "*.txt"))

    if not files:
        print("Не знайдено жодного файлу для обробки!")
    else:
        for file_path in files:
            if args.case == "marketing":
                # Для PDF-файлів маркетингу
                content = extract_text_from_pdf(file_path)
                result = checker(content)
            elif args.case == "complaint":
                transcription = load_transcription(file_path)
                result = checker(transcription, complaint_flag=None)
            else:
                transcription = load_transcription(file_path)
                result = checker(transcription)
            result["file"] = file_path
            save_result_to_csv(result, output_csv)
            print(f"Оброблено: {file_path}")

        print(f"Готово! Всі результати збережено у {output_csv}")


