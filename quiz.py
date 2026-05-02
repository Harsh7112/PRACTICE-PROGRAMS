import json
import time
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent

def load_questions():
    path = SCRIPT_DIR.parent / "question.json"
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def ask_question(q):
    print("\n" + q["question"])
    for i, opt in enumerate(q["options"]):
        print(f"{i+1}, {opt}")

    
    start = time.time()
    try:
        ans = int(input("Your answer: "))
        end = time.time()
        
        if end - start > 10:
            print("Time's up")
            return False
        return q["options"][ans-1]==q["answer"]
    except:
        return False
    

def save_result(name, score, total):
    path = SCRIPT_DIR / "results.txt"
    acc = (score / total) * 100
    with path.open("a", encoding="utf-8") as f:
        f.write(f"{name} | {score}/{total} | {acc}%\n")

def main():
    name = input("Enter your name: ")
    questions = load_questions()

    score = 0

    for q in questions:
        if ask_question(q):
            print("Correct")
            score += 10
        else:
            print("Wrong")

    total = len(questions) * 10
    acc = (score / total) * 100
    print(f"\nScore: {score}/{total}")
    print(f" Accuracy: {acc}%")
    save_result(name, score, total)



if __name__ == "__main__":
    main()