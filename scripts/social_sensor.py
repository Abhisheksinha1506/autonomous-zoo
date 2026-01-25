#!/usr/bin/env python3
"""
Social Metabolism Sensor
Gathers environmental data (Issues/PRs) to feed the repository's organisms.
"""

import json
import subprocess
import os
from pathlib import Path

ENV_FILE = "social_environment.json"

def get_count(command):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return len(result.stdout.strip().split('\n')) if result.stdout.strip() else 0
    except:
        return 0

def sense():
    print("🧠 Sensing social environment...")
    
    # Count open issues
    open_issues = get_count("gh issue list --state open --limit 100")
    
    # Count merged PRs in last 24h (approx)
    merged_prs = get_count("gh pr list --state merged --limit 10")
    
    # Get latest PR contributor if any
    try:
        latest_pr = subprocess.run("gh pr list --state merged --limit 1 --json title,author", 
                                   shell=True, capture_output=True, text=True)
        pr_data = json.loads(latest_pr.stdout)
        contributor = pr_data[0]['author']['login'] if pr_data else "None"
        tagline = pr_data[0]['title'] if pr_data else ""
    except:
        contributor = "None"
        tagline = ""

    environment = {
        "stress_level": min(open_issues * 0.1, 1.0), # 10 issues = max stress
        "nutrient_density": merged_prs * 0.2,        # PRs provide energy
        "latest_mutagen": contributor,
        "mutation_signature": tagline,
        "timestamp": os.getenv("GITHUB_SHA", "local")
    }
    
    with open(ENV_FILE, "w") as f:
        json.dump(environment, f, indent=2)
    
    print(f"✅ Environment updated: Stress={environment['stress_level']:.2f}, Nutrients={environment['nutrient_density']:.2f}")

if __name__ == "__main__":
    sense()
