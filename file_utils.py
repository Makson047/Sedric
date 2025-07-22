def load_transcription(file_path):
    """
    Читає текстовий файл із транскрипцією.
    """
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()