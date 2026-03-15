"""
Utility functions for AutoDraft
"""

import json
from pathlib import Path
from datetime import datetime
from typing import Dict, Any


def load_file(file_path: Path) -> str:
    """Load text content from a file"""
    if not file_path.exists():
        return ""
    return file_path.read_text().strip()


def save_file(file_path: Path, content: str):
    """Save content to a file"""
    file_path.parent.mkdir(parents=True, exist_ok=True)
    file_path.write_text(content)
    print(f"  Saved: {file_path}")


def load_prompt_template(prompt_name: str, project_root: Path) -> str:
    """Load a prompt template from the prompts directory"""
    prompt_path = project_root / "prompts" / f"{prompt_name}.md"
    if not prompt_path.exists():
        raise FileNotFoundError(f"Prompt template not found: {prompt_path}")
    return prompt_path.read_text()


def fill_prompt_template(template: str, **kwargs) -> str:
    """Fill in a prompt template with variables"""
    result = template
    for key, value in kwargs.items():
        placeholder = "{" + key + "}"
        result = result.replace(placeholder, str(value))
    return result


def log_run(log_data: Dict[str, Any], output_dir: Path):
    """Log run information to JSON"""
    log_path = output_dir / "run_log.json"

    # Add timestamp
    log_data["timestamp"] = datetime.now().isoformat()

    # Load existing logs if any
    logs = []
    if log_path.exists():
        try:
            with open(log_path, 'r') as f:
                logs = json.load(f)
        except json.JSONDecodeError:
            logs = []

    # Append new log
    logs.append(log_data)

    # Save
    with open(log_path, 'w') as f:
        json.dump(logs, f, indent=2)

    print(f"  Run logged: {log_path}")


def print_header(text: str, char="="):
    """Print a formatted header"""
    width = 60
    print(char * width)
    print(text)
    print(char * width)


def print_step(step_name: str):
    """Print a step indicator"""
    print(f"\n→ {step_name}...")


def print_success(message: str):
    """Print a success message"""
    print(f"✓ {message}")


def print_error(message: str):
    """Print an error message"""
    print(f"❌ {message}")
