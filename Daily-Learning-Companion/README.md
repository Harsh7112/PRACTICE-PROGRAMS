# 📚 Daily Learning Companion

A beautiful command-line app that gives you a new curated learning topic
every day, tracks your streak, and keeps a history and category-wise
breakdown of everything you've learned — all with **zero external
dependencies**.

```
Daily-Learning-Companion/
│
├── main.py                  # Entry point
├── topics.py                # 1000+ curated topics
├── topic_manager.py         # Random topic + duplicate prevention
├── history.py                # Save learning history (.txt)
├── statistics.py             # Category statistics
├── streak.py                 # Daily streak logic
├── utils.py                  # Helper functions
├── requirements.txt
├── README.md
│
├── data/
│   ├── used_topics.json
│   ├── learning_history.txt
│   ├── statistics.json
│   └── streak.json
│
└── assets/
    └── banner.png
```

## ✨ Features

- ✅ 1,050 curated topics across 15 categories
- ✅ No duplicate topics until all are completed
- ✅ Category display
- ✅ Difficulty levels (Beginner / Intermediate / Advanced)
- ✅ Daily streak tracking
- ✅ Category-wise statistics
- ✅ Learning history export (`.txt`)
- ✅ Beautiful CLI interface
- ✅ Automatic reset after all topics are completed
- ✅ Modular, recruiter-friendly code structure

## 🚀 Getting Started

### Requirements
- Python 3.8+
- No mandatory third-party packages (see `requirements.txt`)

### Run it

```bash
python main.py
```

You'll immediately see today's topic, your current streak, and a menu
to explore statistics and history:

```
[1] Show today's topic
[2] View category statistics
[3] View learning history
[4] View streak
[5] Exit
```

## 🗂️ Main Files

| File | Purpose |
|---|---|
| `main.py` | Runs the application and prints the UI |
| `topics.py` | Contains the topic database (subjects × learning angles → 1,050 topics) |
| `topic_manager.py` | Selects a random unused topic and resets the cycle when needed |
| `history.py` | Appends each learning session to `data/learning_history.txt` |
| `statistics.py` | Maintains per-category / per-difficulty counts in `data/statistics.json` |
| `streak.py` | Tracks consecutive learning days in `data/streak.json` |
| `utils.py` | Date formatting, JSON helpers, progress bar, colors, etc. |

## 🗃️ Data Files

All persistent state lives in `data/` as plain JSON/text so it's easy
to inspect, back up, or reset:

- `used_topics.json` — which topic ids have been shown in the current cycle
- `learning_history.txt` — a running log of every session
- `statistics.json` — cumulative counts by category and difficulty
- `streak.json` — current streak, longest streak, and total days learned

To start completely fresh, simply delete the files inside `data/`
(they're recreated automatically on next run).

## 🧩 How the Topic Database Is Built

Rather than a flat, hand-typed list, `topics.py` combines **15 categories
× 14 real subjects × 5 learning angles** (Fundamentals, History, Key
Concepts, Practical Applications, Advanced Techniques) to generate
**1,050 distinct, readable topics** — e.g. *"Fundamentals of Neural
Networks"*, *"Advanced Techniques in Quantum Computing"* — while keeping
the source code compact and easy to extend. Add a new subject or
category any time by editing `SUBJECTS_BY_CATEGORY` in `topics.py`.

## 🛠️ Extending the App

- Add categories/subjects → edit `SUBJECTS_BY_CATEGORY` in `topics.py`
- Add learning angles/difficulties → edit `ANGLES` in `topics.py`
- Change streak rules → edit `streak.py`
- Change how stats are aggregated → edit `statistics.py`

---
Built as a small, modular, well-documented portfolio project. Happy learning! 🎓
