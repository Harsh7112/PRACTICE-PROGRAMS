"""
utils.py
--------
Small, reusable helper functions shared across the app:
JSON read/write helpers, date formatting, a text progress bar,
screen clearing, and simple colored-text helpers for the CLI.
"""

import os
import json
import sys
from datetime import datetime, date

DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")


# ---------------------------------------------------------------------------
# JSON helpers
# ---------------------------------------------------------------------------

def ensure_data_dir():
    """Make sure the data/ directory exists."""
    os.makedirs(DATA_DIR, exist_ok=True)


def data_path(filename):
    """Return the full path of a file inside the data/ directory."""
    ensure_data_dir()
    return os.path.join(DATA_DIR, filename)


def load_json(filename, default):
    """Load JSON from data/filename, returning `default` if missing/corrupt."""
    path = data_path(filename)
    if not os.path.exists(path):
        return default
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        return default


def save_json(filename, obj):
    """Save `obj` as JSON to data/filename."""
    path = data_path(filename)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, indent=2, ensure_ascii=False)


# ---------------------------------------------------------------------------
# Date helpers
# ---------------------------------------------------------------------------

def today_str():
    """Today's date as YYYY-MM-DD."""
    return date.today().isoformat()


def now_str():
    """Current timestamp as YYYY-MM-DD HH:MM:SS."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def pretty_date(date_string):
    """Convert 'YYYY-MM-DD' into a friendlier 'Jan 05, 2026' format."""
    try:
        d = datetime.strptime(date_string, "%Y-%m-%d")
        return d.strftime("%b %d, %Y")
    except ValueError:
        return date_string


def days_between(date_str_a, date_str_b):
    """Return the absolute number of days between two YYYY-MM-DD dates."""
    d1 = datetime.strptime(date_str_a, "%Y-%m-%d").date()
    d2 = datetime.strptime(date_str_b, "%Y-%m-%d").date()
    return abs((d2 - d1).days)


# ---------------------------------------------------------------------------
# CLI display helpers
# ---------------------------------------------------------------------------

def clear_screen():
    """Clear the terminal screen (cross-platform)."""
    os.system("cls" if os.name == "nt" else "clear")


def progress_bar(current, total, width=30):
    """Return a text progress bar string, e.g. '[#######-----] 58%'."""
    if total <= 0:
        return "[" + ("-" * width) + "] 0%"
    ratio = min(max(current / total, 0), 1)
    filled = int(width * ratio)
    bar = "#" * filled + "-" * (width - filled)
    pct = int(ratio * 100)
    return f"[{bar}] {pct}%"


class Colors:
    """ANSI color codes for a nicer CLI. Falls back gracefully on
    terminals that don't support them (codes are simply ignored)."""
    HEADER = "\033[95m"
    BLUE = "\033[94m"
    CYAN = "\033[96m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    END = "\033[0m"


def colorize(text, color):
    """Wrap `text` in an ANSI color code, if colors are supported."""
    if not sys.stdout.isatty():
        return text
    return f"{color}{text}{Colors.END}"


def print_divider(char="-", width=60):
    print(char * width)


def print_header(title, width=60):
    print_divider("=", width)
    print(colorize(title.center(width), Colors.BOLD + Colors.CYAN))
    print_divider("=", width)
