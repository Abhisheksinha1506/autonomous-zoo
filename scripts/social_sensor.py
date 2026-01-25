#!/usr/bin/env python3
"""
Social Metabolism Sensor (Enhanced)
Gathers environmental data and historical audit trails (merged PRs).
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
    
    # 1. Stress: Count open issues
    open_issues = get_count("gh issue list --state open --limit 100")
    
    # 2. Nutrients: Recent merged PRs
    merged_prs_count = get_count("gh pr list --state merged --limit 10")
    
    # 3. Audit Trail: Get details for last 5 merged PRs
    recent_mutations = []
    try:
        audit_res = subprocess.run("gh pr list --state merged --limit 5 --json number,title,author,mergedAt", 
                                   shell=True, capture_output=True, text=True)
        recent_mutations = json.loads(audit_res.stdout)
    except Exception as e:
        print(f"⚠️ Could not fetch audit trail: {e}")

    environment = {
        "stress_level": min(open_issues * 0.1, 1.0),
        "nutrient_density": merged_prs_count * 0.2,
        "recent_mutations": recent_mutations,
        "latest_mutagen": recent_mutations[0]["author"]["login"] if recent_mutations else "None",
        "mutation_signature": recent_mutations[0]["title"] if recent_mutations else "",
        "timestamp": os.getenv("GITHUB_SHA", "local")
    }
    
    with open(ENV_FILE, "w") as f:
        json.dump(environment, f, indent=2)
    
    print(f"✅ Environment updated with {len(recent_mutations)} mutations in trail.")

if __name__ == "__main__":
    sense()
