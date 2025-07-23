def load_transcription(file_path):
    """
    Reads a text file with a transcription.
    """
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()