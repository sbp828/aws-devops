#!/usr/bin/env python3
"""
generate.py — AWS DevOps Roadmap Automation
"""

import json
from pathlib import Path
from datetime import datetime, timezone

# ---------- PATHS ----------
BASE = Path(__file__).parent
OUTPUT = BASE / "aws-devops"
STATE_FILE = BASE / "data/state/progress.json"
ROADMAP_FILE = BASE / "data/roadmap/roadmap.json"

# ---------- UTILS ----------
def load_json(path):
    with open(path) as f:
        return json.load(f)

def save_text(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content)

def load_state():
    if not STATE_FILE.exists():
        return {"current_day": 0}
    return json.loads(STATE_FILE.read_text())

def save_state(state):
    STATE_FILE.write_text(json.dumps(state, indent=2))

# ---------- CORE ----------
def generate_topic(day_number, topic_name):
    # Folder name: 01-linux, 02-aws, etc. (first word of topic)
    folder_name = f"{day_number:02d}-{topic_name.split()[0].lower()}"
    topic_folder = OUTPUT / folder_name
    topic_folder.mkdir(parents=True, exist_ok=True)

    # 3 files inside folder
    notes_content = f"# {topic_name}\nGenerated on {datetime.now(timezone.utc).isoformat()} UTC\n\nNotes placeholder"
    commands_content = f"# {topic_name} Commands\n- command1\n- command2\n- command3"
    poc_content = f"# PoC for {topic_name}\n- Step 1\n- Step 2\n- Step 3"

    save_text(topic_folder / "01-notes.md", notes_content)
    save_text(topic_folder / "02-commands.md", commands_content)
    save_text(topic_folder / "03-poc.md", poc_content)

    print(f"[OK] Topic generated: {folder_name}")

# ---------- ENGINE ----------
def main():
    roadmap = load_json(ROADMAP_FILE)
    state = load_state()
    current_day = state.get("current_day", 0)

    if current_day >= len(roadmap):
        print("[INFO] All topics already generated!")
        return

    # Generate topic
    topic_name = roadmap[current_day]
    generate_topic(current_day + 1, topic_name)

    # Update state
    state["current_day"] = current_day + 1
    state["last_run"] = datetime.now(timezone.utc).isoformat()
    save_state(state)

if __name__ == "__main__":
    main()
