#!/curriculum-gap-analyzer.py
"""
Curriculum Gap Analyzer
Identifies missing assignment topics from the current curriculum.
"""

import json
from pathlib import Path
from typing import List, Dict, Set

# Core Python fundamentals progression
CURRICULUM_ROADMAP = {
    "Beginner": [
        "python-basics",
        "control-flow",
        "functions",
        "data-structures",
    ],
    "Intermediate": [
        "python-classes",
        "file-io",
        "error-handling",
        "working-with-libraries",
        "games-in-python",
    ],
    "Advanced": [
        "data-analysis",
        "web-frameworks",
        "fastapi-rest-api",
        "web-scraping",
        "testing-debugging",
    ],
    "Expert": [
        "async-programming",
        "machine-learning",
        "databases",
        "cli-tools",
        "performance-optimization",
    ],
}

TOPIC_DESCRIPTIONS = {
    "python-basics": "Variables, data types, conditionals, loops",
    "control-flow": "Advanced control flow, iteration patterns",
    "functions": "Function definitions, scoping, recursion",
    "data-structures": "Lists, dicts, sets, comprehensions",
    "python-classes": "OOP, inheritance, encapsulation",
    "file-io": "Reading/writing files, working with formats (JSON, CSV)",
    "error-handling": "Exception handling, custom exceptions, logging",
    "working-with-libraries": "Importing packages, pip, virtual environments",
    "games-in-python": "Game logic, state management, user interaction",
    "data-analysis": "Pandas, NumPy, data exploration, visualization",
    "web-frameworks": "Web development, routing, templating",
    "fastapi-rest-api": "REST APIs, HTTP methods, data validation",
    "web-scraping": "HTTP requests, parsing HTML, data extraction",
    "testing-debugging": "Unit tests, pytest, debugging, TDD",
    "async-programming": "Asyncio, concurrent programming, performance",
    "machine-learning": "scikit-learn, model training, prediction",
    "databases": "SQL, ORMs, data persistence",
    "cli-tools": "Click, argparse, building command-line tools",
    "performance-optimization": "Profiling, optimization, scalability",
}


def load_config(config_path: str) -> Dict:
    """Load the curriculum config."""
    with open(config_path, "r") as f:
        return json.load(f)


def get_current_topics(config: Dict) -> Set[str]:
    """Extract topic IDs from current assignments."""
    return {assignment["id"] for assignment in config.get("assignments", [])}


def find_gaps(current_topics: Set[str]) -> Dict[str, List[str]]:
    """Identify missing topics by level."""
    gaps = {}
    for level, topics in CURRICULUM_ROADMAP.items():
        missing = [t for t in topics if t not in current_topics]
        if missing:
            gaps[level] = missing
    return gaps


def print_curriculum_status():
    """Print detailed curriculum analysis."""
    config_path = "config.json"
    
    try:
        config = load_config(config_path)
        current_topics = get_current_topics(config)
        gaps = find_gaps(current_topics)
        
        print("\n" + "=" * 70)
        print("CURRICULUM GAP ANALYSIS")
        print("=" * 70)
        
        print(f"\n✅ CURRENT ASSIGNMENTS ({len(current_topics)}):")
        for topic in sorted(current_topics):
            desc = TOPIC_DESCRIPTIONS.get(topic, "No description")
            print(f"   • {topic}: {desc}")
        
        if gaps:
            print(f"\n⚠️  MISSING TOPICS BY LEVEL:")
            for level in ["Beginner", "Intermediate", "Advanced", "Expert"]:
                if level in gaps:
                    print(f"\n   {level}:")
                    for topic in gaps[level]:
                        desc = TOPIC_DESCRIPTIONS.get(topic, "No description")
                        print(f"      ○ {topic}: {desc}")
        else:
            print("\n✨ All recommended topics are covered!")
        
        print("\n" + "=" * 70)
        print("RECOMMENDATION:")
        if gaps and "Intermediate" in gaps:
            first_gap = gaps["Intermediate"][0]
            print(f"   Next assignment: {first_gap}")
            print(f"   Description: {TOPIC_DESCRIPTIONS[first_gap]}")
        elif gaps:
            for level in ["Beginner", "Advanced", "Expert"]:
                if level in gaps:
                    first_gap = gaps[level][0]
                    print(f"   Next assignment ({level}): {first_gap}")
                    print(f"   Description: {TOPIC_DESCRIPTIONS[first_gap]}")
                    break
        print("=" * 70 + "\n")
        
    except FileNotFoundError:
        print(f"Error: {config_path} not found")
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON in {config_path}")


if __name__ == "__main__":
    print_curriculum_status()