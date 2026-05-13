import os


def ensure_output_dir(path: str):
    os.makedirs(path, exist_ok=True)
