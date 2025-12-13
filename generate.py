import json
from pathlib import Path
from datetime import datetime

# Files
ROADMAP_FILE = Path("roadmap.json")
STATE_FILE = Path(".state")

# Base output directory
BASE_DIR = Path("aws-devops")

# Load roadmap
topics = json.loads(ROADMAP_FILE.read_text())

# Load state
current_index = int(STATE_FILE.read_text()) if STATE_FILE.exists() else 0

# Stop if roadmap completed
if current_index >= len(topics):
    exit(0)

topic = topics[current_index]
safe_topic = topic.lower().replace(" ", "-")

# Folder structure
phase_folder = f"{current_index + 1:02d}-{safe_topic.split('-')[0]}"
topic_dir = BASE_DIR / phase_folder
topic_dir.mkdir(parents=True, exist_ok=True)

# Note file
note_file = topic_dir / f"{safe_topic}.md"

note_file.write_text(f"""# {topic}

## Date
{datetime.utcnow().date()}

## Objective
Learn and understand {topic}

## Notes
- Overview
- Key concepts
- Common commands
- Real-world usage

## Status
Draft
""")

# Update state
STATE_FILE.write_text(str(current_index + 1))
