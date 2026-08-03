"""
main.py
-------
Entry point for the Daily Learning Companion CLI application.

Run with:
    python main.py
"""

import sys

import topic_manager
import history
import statistics
import streak
from topics import CATEGORIES
from utils import (
    clear_screen, colorize, print_header, print_divider,
    progress_bar, Colors, today_str,
)

APP_NAME = "Daily Learning Companion"
BANNER = r"""
  _____        _ _         _                          _
 |  __ \      (_) |       | |                        (_)
 | |  | | __ _ _| |_   _  | |     ___  __ _ _ __ _ __  _ _ __   __ _
 | |  | |/ _` | | | | | | | |    / _ \/ _` | '__| '_ \| | '_ \ / _` |
 | |__| | (_| | | | |_| | | |___|  __/ (_| | |  | | | | | | | | (_| |
 |_____/ \__,_|_|_|\__, | |______\___|\__,_|_|  |_| |_|_|_| |_|\__, |
                     __/ |                                     __/ |
                    |___/    Companion                         |___/
"""


def show_banner():
    print(colorize(BANNER, Colors.CYAN))
    print(colorize(f"{APP_NAME} — {today_str()}".center(70), Colors.BOLD))
    print_divider("=", 70)


def show_todays_topic():
    topic, is_new_pick, reset_happened = topic_manager.get_todays_topic()

    # Only log/record/update the streak the first time this topic is
    # picked for the day. Re-viewing it later (e.g. via the menu) must
    # NOT duplicate history entries or inflate the statistics.
    if is_new_pick:
        history.log_session(topic)
        statistics.record_topic(topic)
        streak.update_streak()

    cur, longest, total_days = streak.get_streak_summary()

    if reset_happened:
        print(colorize(
            "\n🎉 You've completed every topic in the library! "
            "Starting a brand-new cycle.\n", Colors.GREEN + Colors.BOLD
        ))

    print()
    print(colorize(" TODAY'S TOPIC ", Colors.BOLD + Colors.HEADER).center(70))
    print_divider("-", 70)
    print(f"  📚 Category   : {colorize(topic['category'], Colors.BLUE)}")
    print(f"  🎯 Difficulty : {colorize(topic['difficulty'], Colors.YELLOW)}")
    print(f"  💡 Topic      : {colorize(topic['topic'], Colors.GREEN + Colors.BOLD)}")
    print_divider("-", 70)

    completed, total = topic_manager.get_progress()
    print(f"\n  Progress this cycle: {progress_bar(completed, total)} "
          f"({completed}/{total} topics)")
    print(f"  🔥 Current streak: {cur} day(s)  |  🏆 Longest streak: {longest} day(s)")
    print()


def show_statistics():
    stats = statistics.load_stats()
    print()
    print_header("CATEGORY STATISTICS")
    print(f"\n  Total topics completed (all-time): {stats['total_completed']}\n")

    print(colorize("  By Category:", Colors.BOLD))
    for cat in CATEGORIES:
        count = stats["by_category"].get(cat, 0)
        print(f"    {cat:<22} {progress_bar(count, max(stats['total_completed'], 1), 20)} {count}")

    print(colorize("\n  By Difficulty:", Colors.BOLD))
    for diff in ("Beginner", "Intermediate", "Advanced"):
        count = stats["by_difficulty"].get(diff, 0)
        print(f"    {diff:<15} {count}")
    print()


def show_history():
    print()
    print_header("LEARNING HISTORY (most recent first)")
    entries = history.read_history(limit=20)
    if not entries:
        print("\n  No learning history yet — come back after your first session!\n")
        return
    print()
    for line in entries:
        print(f"  {line}")
    total = history.history_count()
    if total > 20:
        print(f"\n  ...and {total - 20} more entries in data/learning_history.txt")
    print()


def show_streak():
    cur, longest, total_days = streak.get_streak_summary()
    print()
    print_header("STREAK TRACKER")
    print(f"\n  🔥 Current streak : {cur} day(s)")
    print(f"  🏆 Longest streak : {longest} day(s)")
    print(f"  📅 Total days learned : {total_days}")
    print()


def show_menu():
    print_divider("-", 70)
    print("  [1] Show today's topic")
    print("  [2] View category statistics")
    print("  [3] View learning history")
    print("  [4] View streak")
    print("  [5] Exit")
    print_divider("-", 70)


def main():
    clear_screen()
    show_banner()
    show_todays_topic()

    while True:
        show_menu()
        choice = input("  Choose an option (1-5): ").strip()

        if choice == "1":
            show_todays_topic()
        elif choice == "2":
            show_statistics()
        elif choice == "3":
            show_history()
        elif choice == "4":
            show_streak()
        elif choice == "5":
            print(colorize("\n  Keep learning — see you tomorrow! 👋\n", Colors.CYAN))
            sys.exit(0)
        else:
            print(colorize("\n  Invalid choice, please enter a number from 1-5.\n", Colors.RED))


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(colorize("\n\n  Session ended. See you tomorrow! 👋\n", Colors.CYAN))
        sys.exit(0)
