"""
statistics.py
-------------
Maintains category-wise learning statistics in data/statistics.json:
how many topics have been completed per category, per difficulty,
and overall, so the user can see their progress at a glance.
"""

from utils import load_json, save_json
from topics import CATEGORIES

STATS_FILE = "statistics.json"


def _default_stats():
    return {
        "total_completed": 0,
        "by_category": {cat: 0 for cat in CATEGORIES},
        "by_difficulty": {"Beginner": 0, "Intermediate": 0, "Advanced": 0},
    }


def load_stats():
    stats = load_json(STATS_FILE, _default_stats())
    # Make sure any newly added categories are represented too.
    for cat in CATEGORIES:
        stats["by_category"].setdefault(cat, 0)
    for diff in ("Beginner", "Intermediate", "Advanced"):
        stats["by_difficulty"].setdefault(diff, 0)
    return stats


def save_stats(stats):
    save_json(STATS_FILE, stats)


def record_topic(topic):
    """Increment counters after a topic has been shown/learned."""
    stats = load_stats()
    stats["total_completed"] += 1
    stats["by_category"][topic["category"]] = (
        stats["by_category"].get(topic["category"], 0) + 1
    )
    stats["by_difficulty"][topic["difficulty"]] = (
        stats["by_difficulty"].get(topic["difficulty"], 0) + 1
    )
    save_stats(stats)
    return stats


def top_categories(n=5):
    """Return the top `n` categories by number of topics completed."""
    stats = load_stats()
    ranked = sorted(
        stats["by_category"].items(), key=lambda kv: kv[1], reverse=True
    )
    return ranked[:n]
