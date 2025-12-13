#!/usr/bin/env python3
import os
import json
from datetime import datetime, timezone

# Paths
ROADMAP_FILE = "data/roadmap/roadmap.json"
STATE_FILE = "data/state/progress.json"
OUTPUT_DIR = "aws-devops"

# Ensure output directories exist
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(os.path.dirname(STATE_FILE), exist_ok=True)

# Load roadmap JSON
def load_json(path):
    with open(path) as f:
        return json.load(f)

# Load progress state
def load_state(path):
    if os.path.exists(path):
        with open(path) as f:
            return json.load(f)
    return {}

# Save progress state
def save_state(path, state):
    with open(path, "w") as f:
        json.dump(state, f, indent=2)

# Generate topic files
def generate_topic_files(topic_name, category_folder):
    os.makedirs(category_folder, exist_ok=True)
    base_name = topic_name.lower().replace(" ", "-")
    filenames = [
        f"{base_name}-notes.md",
        f"{base_name}-commands.md",
        f"{base_name}-poc.md"
    ]
    for filename in filenames:
        filepath = os.path.join(category_folder, filename)
        if not os.path.exists(filepath):
            with open(filepath, "w") as f:
                f.write(f"# {topic_name}\nGenerated on {datetime.now(timezone.utc).isoformat()} UTC\n")
    return filenames

def main():
    roadmap = load_json(ROADMAP_FILE)
    state = load_state(STATE_FILE)

    for idx, topic in enumerate(roadmap, 1):
        # Determine category (first word)
        category = topic.split()[0].lower()
        category_folder = os.path.join(OUTPUT_DIR, f"{idx:02d}-{category}")

        # Generate files inside category folder
        files_created = generate_topic_files(topic, category_folder)
        print(f"[OK] Topic generated: {topic} in {category_folder}")

        # Update state
        state[topic] = {
            "folder": category_folder,
            "files": files_created,
            "timestamp": datetime.now(timezone.utc).isoformat()
        }

    save_state(STATE_FILE, state)
    print("[OK] All topics processed successfully!")

if __name__ == "__main__":
    main()
