import json
import os
from dataclasses import asdict

from src.exceptions import WriterError
from src.utils import ensure_output_dir


def write_json(videos, output_file: str):
    try:
        ensure_output_dir(os.path.dirname(output_file))
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump([asdict(v) for v in videos], f, ensure_ascii=False, indent=2)
    except Exception as exc:
        raise WriterError(str(exc)) from exc
