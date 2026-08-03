"""
topics.py
---------
Curated topic database for the Daily Learning Companion.

Topics are built from a set of hand-picked subjects across 15 broad
categories, each explored through 5 different "learning angles"
(fundamentals, history, key concepts, practical applications, and
advanced techniques). This keeps the database large (1000+ entries)
while every entry still reads as a genuine, specific learning topic.

Each topic is a dict:
    {
        "id": int,             # stable unique identifier
        "category": str,       # e.g. "Programming"
        "topic": str,          # e.g. "Fundamentals of Python"
        "difficulty": str,     # "Beginner" | "Intermediate" | "Advanced"
    }
"""

# ---------------------------------------------------------------------------
# 1. Subjects grouped by category (14 subjects per category)
# ---------------------------------------------------------------------------

SUBJECTS_BY_CATEGORY = {
    "Programming": [
        "Python", "JavaScript", "Object-Oriented Programming",
        "Functional Programming", "Data Structures", "Algorithms",
        "Version Control (Git)", "Web Development", "APIs", "Databases",
        "Software Testing", "Design Patterns", "Concurrency", "Debugging",
    ],
    "Science": [
        "Physics", "Chemistry", "Biology", "Genetics", "Thermodynamics",
        "Quantum Mechanics", "Evolution", "Ecology", "Microbiology",
        "Astrophysics", "Geology", "Meteorology", "Neuroscience",
        "Biochemistry",
    ],
    "Mathematics": [
        "Algebra", "Calculus", "Geometry", "Probability", "Statistics",
        "Number Theory", "Linear Algebra", "Trigonometry",
        "Discrete Mathematics", "Graph Theory", "Set Theory",
        "Mathematical Logic", "Topology", "Game Theory",
    ],
    "History": [
        "Ancient Egypt", "The Roman Empire", "World War I", "World War II",
        "The Renaissance", "The Cold War", "The Industrial Revolution",
        "The French Revolution", "Ancient Greece", "Medieval Europe",
        "Colonialism", "The Civil Rights Movement", "The Silk Road",
        "The Byzantine Empire",
    ],
    "Technology": [
        "Artificial Intelligence", "Machine Learning", "Blockchain",
        "Cloud Computing", "Cybersecurity", "The Internet of Things",
        "Virtual Reality", "Robotics", "5G Networks", "Quantum Computing",
        "Big Data", "Augmented Reality", "Semiconductors",
        "Autonomous Vehicles",
    ],
    "Business": [
        "Marketing", "Entrepreneurship", "Supply Chain Management",
        "Corporate Finance", "Negotiation", "Leadership", "Branding",
        "E-commerce", "Business Strategy", "Human Resources", "Sales",
        "Project Management", "Accounting", "Venture Capital",
    ],
    "Health & Fitness": [
        "Nutrition", "Cardiovascular Exercise", "Strength Training",
        "Mental Health", "Sleep Science", "Yoga", "The Immune System",
        "Weight Management", "Stress Management", "Public Health",
        "Aging", "Hydration", "Injury Prevention", "Mindfulness",
    ],
    "Arts & Culture": [
        "Renaissance Art", "Modern Art", "Classical Music", "Jazz",
        "Filmmaking", "Photography", "Architecture", "Sculpture", "Dance",
        "Theatre", "Fashion Design", "Street Art", "Opera", "Ceramics",
    ],
    "Philosophy": [
        "Ethics", "Existentialism", "Stoicism", "Epistemology", "Logic",
        "Metaphysics", "Political Philosophy", "Philosophy of Mind",
        "Utilitarianism", "Nihilism", "Eastern Philosophy",
        "Philosophy of Science", "Aesthetics", "Free Will",
    ],
    "Psychology": [
        "Cognitive Psychology", "Behavioral Psychology",
        "Developmental Psychology", "Social Psychology",
        "Personality Theory", "Memory", "Motivation",
        "Emotional Intelligence", "Psychoanalysis", "Positive Psychology",
        "Neuropsychology", "Group Dynamics", "Perception", "Learning Theory",
    ],
    "Space & Astronomy": [
        "The Solar System", "Black Holes", "Galaxies", "Space Exploration",
        "The Moon Landing", "Exoplanets", "The Big Bang",
        "Stars and Stellar Evolution", "Mars Exploration", "Satellites",
        "Cosmology", "The International Space Station",
        "Comets and Asteroids", "Dark Matter",
    ],
    "Environment": [
        "Climate Change", "Renewable Energy", "Biodiversity",
        "Deforestation", "Ocean Conservation", "Sustainable Agriculture",
        "Recycling", "Air Pollution", "Water Conservation",
        "Wildlife Conservation", "Carbon Footprint", "Green Building",
        "Environmental Policy", "Ecosystem Services",
    ],
    "Economics": [
        "Supply and Demand", "Inflation", "Macroeconomics",
        "Microeconomics", "International Trade", "Behavioral Economics",
        "Monetary Policy", "Fiscal Policy", "Labor Markets",
        "Economic Growth", "Market Structures", "Cryptocurrency Economics",
        "Game Theory in Economics", "Income Inequality",
    ],
    "Literature": [
        "Shakespearean Plays", "Modernist Literature", "Poetry Analysis",
        "Science Fiction", "Literary Criticism", "The Novel Form",
        "Mythology", "Postcolonial Literature", "Magical Realism",
        "Short Stories", "Literary Symbolism", "World Literature",
        "Gothic Literature", "Narrative Structure",
    ],
    "Language Learning": [
        "Grammar Fundamentals", "Vocabulary Building", "Pronunciation",
        "Language Immersion", "Bilingualism", "Sign Language", "Etymology",
        "Language Families", "Translation", "Idioms and Expressions",
        "Language Acquisition", "Phonetics", "Writing Systems",
        "Conversational Fluency",
    ],
}

# ---------------------------------------------------------------------------
# 2. Learning angles applied to every subject, each with its own difficulty
# ---------------------------------------------------------------------------

ANGLES = [
    ("Fundamentals of {subject}", "Beginner"),
    ("History of {subject}", "Beginner"),
    ("Key Concepts in {subject}", "Intermediate"),
    ("Practical Applications of {subject}", "Intermediate"),
    ("Advanced Techniques in {subject}", "Advanced"),
]


def _build_topics():
    """Builds the full list of topic dicts from subjects x angles."""
    topics = []
    topic_id = 1
    for category, subjects in SUBJECTS_BY_CATEGORY.items():
        for subject in subjects:
            for template, difficulty in ANGLES:
                topics.append({
                    "id": topic_id,
                    "category": category,
                    "topic": template.format(subject=subject),
                    "difficulty": difficulty,
                })
                topic_id += 1
    return topics


# The final topic database, generated once at import time.
TOPICS = _build_topics()

# Convenience lookups
CATEGORIES = list(SUBJECTS_BY_CATEGORY.keys())
TOTAL_TOPICS = len(TOPICS)


if __name__ == "__main__":
    print(f"Total topics generated: {TOTAL_TOPICS}")
    print(f"Total categories: {len(CATEGORIES)}")
    for cat in CATEGORIES:
        count = sum(1 for t in TOPICS if t["category"] == cat)
        print(f"  {cat}: {count} topics")
