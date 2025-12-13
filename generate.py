import json
import os
from datetime import datetime, timezone

BASE_DIR = "aws-devops"
STATE_FILE = ".state.json"

ROADMAP_PATHS = [
    "aws-devops/roadmap.json",
    "data/roadmap.json"
]

FILES = ["notes.md", "commands.md", "poc.md"]


def load_roadmap():
    for path in ROADMAP_PATHS:
        if os.path.exists(path):
            with open(path) as f:
                return json.load(f)
    raise FileNotFoundError("roadmap.json not found in aws-devops/ or data/")


def load_state():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE) as f:
            return json.load(f)
    return {"current_index": 0}


def save_state(state):
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)


def detect_category(topic: str) -> str:
    t = topic.lower().strip()

    if t.startswith("linux"):
        return "linux"
    if t.startswith("aws"):
        return "aws"
    if t.startswith("docker"):
        return "docker"
    if t.startswith("kubernetes") or t.startswith("k8s"):
        return "kubernetes"
    if t.startswith("terraform"):
        return "terraform"
    if t.startswith("ci") or t.startswith("jenkins") or t.startswith("github"):
        return "cicd"

    return "misc"


def update_files(folder, topic):
    os.makedirs(folder, exist_ok=True)
    timestamp = datetime.now(timezone.utc).isoformat()

    for file in FILES:
        path = os.path.join(folder, file)
        with open(path, "a") as f:
            f.write(f"\n## {topic}\n")
            f.write(f"- Updated at: {timestamp}\n")


def main():
    roadmap = load_roadmap()
    state = load_state()

    index = state["current_index"]
    if index >= len(roadmap):
        print("[INFO] Roadmap completed")
        return

    topic = roadmap[index]
    category = detect_category(topic)

    folder = os.path.join(BASE_DIR, category)
    update_files(folder, topic)

    print(f"[OK] Topic {index + 1}: {topic} → {category}/")

    state["current_index"] += 1
    save_state(state)


if __name__ == "__main__":
    main()
