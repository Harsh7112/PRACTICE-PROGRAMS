"""
streak.py
---------
Tracks consecutive daily learning streaks in data/streak.json.

Rules:
- Learning on a new day that is exactly 1 day after the last
  recorded day extends the streak.
- Learning again on the same day keeps the streak unchanged.
- Learning after a gap of 2+ days resets the streak to 1.
"""

from utils import load_json, save_json, today_str, days_between

STREAK_FILE = "streak.json"


def _default_streak():
    return {
        "current_streak": 0,
        "longest_streak": 0,
        "last_learned_date": None,
        "total_days_learned": 0,
    }


def load_streak():
    return load_json(STREAK_FILE, _default_streak())


def save_streak(streak):
    save_json(STREAK_FILE, streak)


def update_streak():
    """
    Call once per day when the user engages with the app.
    Returns (streak_dict, is_new_day) where is_new_day tells the
    caller whether the streak actually changed today.
    """
    streak = load_streak()
    today = today_str()
    last = streak["last_learned_date"]

    if last == today:
        return streak, False  # already recorded today

    if last is None:
        streak["current_streak"] = 1
    else:
        gap = days_between(last, today)
        if gap == 1:
            streak["current_streak"] += 1
        else:
            streak["current_streak"] = 1

    streak["longest_streak"] = max(streak["longest_streak"], streak["current_streak"])
    streak["last_learned_date"] = today
    streak["total_days_learned"] += 1

    save_streak(streak)
    return streak, True


def get_streak_summary():
    streak = load_streak()
    return (
        streak["current_streak"],
        streak["longest_streak"],
        streak["total_days_learned"],
    )
