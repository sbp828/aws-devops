#!/usr/bin/env python3
import os
import json
from datetime import datetime, timezone

# Paths
ROADMAP_FILE = "data/roadmap/roadmap.json"
OUTPUT_DIR = "aws-devops"
STATE_FILE = "data/state/progress.json"

# Load roadmap JSON
def load_json(path):
    with open(path) as f:
        return json.load(f)

# Load state (last run info)
def load_state(path):
    if not os.path.exists(path):
        return {}
    with open(path) as f:
        return json.load(f)

# Save state
def save_state(path, state):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        json.dump(state, f, indent=2)

# Generate files for a topic
def generate_topic(topic_number, topic_name, state):
    folder_name = f"{str(topic_number).zfill(2)}-{topic_name.lower().replace(' ', '-')}"
    folder_path = os.path.join(OUTPUT_DIR, folder_name)
    os.makedirs(folder_path, exist_ok=True)

    files = ["notes.md", "commands.md", "poc.md"]

    for i, filename in enumerate(files, start=1):
        file_path = os.path.join(folder_path, f"{str(i).zfill(2)}-{filename}")
        if not os.path.exists(file_path):
            content = f"# {topic_name} - {filename.replace('.md', '').title()}\n\n"
            content += f"Generated on {datetime.now(timezone.utc).isoformat()} UTC\n"
            with open(file_path, "w") as f:
                f.write(content)
            print(f"[OK] Topic file generated: {file_path}")

    state[folder_name] = {"last_run": datetime.now(timezone.utc).isoformat()}

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    roadmap = load_json(ROADMAP_FILE)
    state = load_state(STATE_FILE)

    for idx, topic in enumerate(roadmap, start=1):
        generate_topic(idx, topic, state)

    save_state(STATE_FILE, state)
    print("[OK] All topics processed successfully!")

if __name__ == "__main__":
    main()
