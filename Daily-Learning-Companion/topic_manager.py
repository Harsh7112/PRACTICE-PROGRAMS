"""
topic_manager.py
----------------
Responsible for picking a random, not-yet-seen topic from the
curated database in topics.py. Tracks which topic ids have already
been shown in data/used_topics.json so the same topic never repeats
until every topic has been covered, at which point it automatically
resets and starts a fresh cycle.
"""

import random

from topics import TOPICS, TOTAL_TOPICS
from utils import load_json, save_json, today_str

USED_TOPICS_FILE = "used_topics.json"


def _default_state():
    return {
        "used_ids": [],       # topic ids already shown in the current cycle
        "cycle_count": 0,     # how many full cycles have been completed
        "last_shown_date": None,
        "last_topic_id": None,
    }


def load_state():
    """Load the used-topics tracking state from disk."""
    return load_json(USED_TOPICS_FILE, _default_state())


def save_state(state):
    save_json(USED_TOPICS_FILE, state)


def get_topic_by_id(topic_id):
    for t in TOPICS:
        if t["id"] == topic_id:
            return t
    return None


def get_todays_topic():
    """
    Return today's topic.

    - If a topic was already selected today, return that same one
      (so re-running the app the same day doesn't skip topics).
    - Otherwise, pick a random topic that hasn't been used in the
      current cycle, mark it as used, and return it.
    - If every topic has been used, reset the cycle automatically.
    """
    state = load_state()
    today = today_str()

    # Already picked a topic today? Return it again, but flag it as
    # NOT a new pick so the caller doesn't re-log/re-count it.
    if state["last_shown_date"] == today and state["last_topic_id"] is not None:
        topic = get_topic_by_id(state["last_topic_id"])
        if topic:
            return topic, False, False  # (topic, is_new_pick, reset_happened)

    used_ids = set(state["used_ids"])
    remaining = [t for t in TOPICS if t["id"] not in used_ids]

    reset_happened = False
    if not remaining:
        # Completed a full cycle through all topics — reset and start over.
        state["used_ids"] = []
        state["cycle_count"] += 1
        remaining = TOPICS
        reset_happened = True

    topic = random.choice(remaining)

    state["used_ids"].append(topic["id"])
    state["last_shown_date"] = today
    state["last_topic_id"] = topic["id"]
    save_state(state)

    return topic, True, reset_happened


def get_progress():
    """Return (completed_count, total_count) for the current cycle."""
    state = load_state()
    return len(state["used_ids"]), TOTAL_TOPICS


def get_cycle_count():
    return load_state()["cycle_count"]
