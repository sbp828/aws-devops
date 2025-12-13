import json
from pathlib import Path
from datetime import datetime, timezone

BASE_DIR = Path(__file__).parent
CONTENT_DIR = BASE_DIR / "aws-devops"
ROADMAP_PATHS = [
    BASE_DIR / "data" / "roadmap" / "roadmap.json",
    BASE_DIR / "aws-devops" / "roadmap.json"
]
STATE_FILE = BASE_DIR / ".state.json"


def load_roadmap():
    for path in ROADMAP_PATHS:
        if path.exists():
            with open(path) as f:
                return json.load(f)
    raise FileNotFoundError("roadmap.json not found in aws-devops/ or data/")


def load_state():
    if STATE_FILE.exists():
        return json.loads(STATE_FILE.read_text())
    return {"index": 0}


def save_state(state):
    STATE_FILE.write_text(json.dumps(state, indent=2))


def detect_category(topic: str) -> str:
    t = topic.lower()
    if t.startswith("linux"):
        return "linux"
    if t.startswith("aws"):
        return "aws"
    if t.startswith("docker"):
        return "docker"
    if t.startswith("kubernetes"):
        return "kubernetes"
    if t.startswith("terraform"):
        return "terraform"
    if "ci cd" in t or "github actions" in t or "jenkins" in t:
        return "cicd"
    return "misc"


def append_section(file_path: Path, topic: str, content: str):
    with open(file_path, "a") as f:
        f.write(f"\n\n## {topic}\n")
        f.write(content.strip() + "\n")


def main():
    roadmap = load_roadmap()
    state = load_state()

    if state["index"] >= len(roadmap):
        print("[OK] All topics processed successfully!")
        return

    topic = roadmap[state["index"]]
    category = detect_category(topic)

    category_dir = CONTENT_DIR / category
    category_dir.mkdir(parents=True, exist_ok=True)

    notes = category_dir / "notes.md"
    commands = category_dir / "commands.md"
    poc = category_dir / "poc.md"

    timestamp = datetime.now(timezone.utc).isoformat()

    append_section(
        notes,
        topic,
        f"- Learned concepts related to **{topic}**\n- Study timestamp: {timestamp}"
    )

    append_section(
        commands,
        topic,
        f"- Example commands for **{topic}**\n- (Add real commands here later)"
    )

    append_section(
        poc,
        topic,
        f"- Proof of concept ideas for **{topic}**\n- (Scripts / configs later)"
    )

    state["index"] += 1
    save_state(state)

    print(f"[OK] Topic {state['index']}: {topic} → {category}/")


if __name__ == "__main__":
    main()
