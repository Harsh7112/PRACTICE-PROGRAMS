"""
history.py
----------
Appends each learning session to a human-readable text file
(data/learning_history.txt) and provides a helper to read it back
for display inside the CLI.
"""

import os

from utils import data_path, now_str, ensure_data_dir

HISTORY_FILE = "learning_history.txt"


def log_session(topic):
    """Append one learning session entry to the history text file."""
    ensure_data_dir()
    path = data_path(HISTORY_FILE)
    line = (
        f"[{now_str()}] "
        f"Category: {topic['category']:<20} | "
        f"Difficulty: {topic['difficulty']:<12} | "
        f"Topic: {topic['topic']}\n"
    )
    with open(path, "a", encoding="utf-8") as f:
        f.write(line)


def read_history(limit=None):
    """
    Return the learning history as a list of lines (most recent first).
    If `limit` is given, only the most recent `limit` entries are returned.
    """
    path = data_path(HISTORY_FILE)
    if not os.path.exists(path):
        return []
    with open(path, "r", encoding="utf-8") as f:
        lines = [line.rstrip("\n") for line in f if line.strip()]
    lines.reverse()
    if limit:
        lines = lines[:limit]
    return lines


def history_count():
    """Return the total number of logged sessions."""
    return len(read_history())


def clear_history():
    """Delete the history file (used only if the user explicitly resets)."""
    path = data_path(HISTORY_FILE)
    if os.path.exists(path):
        os.remove(path)
