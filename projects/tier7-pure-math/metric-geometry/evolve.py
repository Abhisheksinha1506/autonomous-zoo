#!/usr/bin/env python3
"""
Metric Geometry
Explores non-Euclidean distance metrics in file organization (Taxi-cab vs L2).
"""

import json
import math
from pathlib import Path

def get_social_environment():
    """Reads global social data (Issues/PRs)."""
    try:
        env_path = Path(__file__).parent
        for _ in range(5):
            target = env_path / "social_environment.json"
            if target.exists():
                with open(target) as f: return json.load(f)
            env_path = env_path.parent
    except: pass
    return {"stress_level": 0.0, "nutrient_density": 0.0, "mutation_signature": ""}








def taxicab(p1, p2):
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

def euclidean(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def load_state():
    defaults = {"generation": 0, "p1": [0,0], "p2": [3,4]}
    if Path("state.json").exists():
        with open("state.json") as f:
            try:
                state = json.load(f)
                defaults.update(state)
            except: pass
    return defaults

def evolve_step(state):
    env = get_social_environment()
    state["generation"] += 1
    # Drift the points
    state["p2"][0] += 1
    state["p2"][1] += (state["generation"] % 2)
    
    p1, p2 = state["p1"], state["p2"]
    state["d_taxi"] = taxicab(p1, p2)
    state["d_eucl"] = round(euclidean(p1, p2), 4)
    return state


def update_readme(summary):
    readme_path = Path("README.md")
    if not readme_path.exists(): return
    try:
        content = readme_path.read_text()
        start = "<!-- LATEST_STATUS_START -->"
        end = "<!-- LATEST_STATUS_END -->"
        if start not in content or end not in content: return
        parts = content.split(start)
        suffix_parts = parts[1].split(end)
        prefix = parts[0] + start
        suffix = end + suffix_parts[1]
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        new_inner = f"
*{summary} ({timestamp})*
"
        readme_path.write_text(prefix + new_inner + suffix)
    except Exception as e: print(f"⚠️ README Update Failed: {e}")

def main():
    env = get_social_environment()
    print("🧬 Metric Geometry - Evolution Step")
    state = load_state()
    state = evolve_step(state)
    
    # Create human-readable summary
    summary = "Two digital points drifted through the repo's topological space today. "
    
    summary += f"The project compared how far they moved using two different 'yardsticks': the blocky Taxicab metric ({state['d_taxi']} units) and the straight-line Euclidean metric ({state['d_eucl']} units)."

    with open("state.json", "w") as f:
        json.dump(state, f)
        
    with open("metrics.md", "a") as f:
        if state["generation"] == 1: f.write("# Topological Distance Metrics\n\n")
        f.write(f"## Generation {state['generation']}\n")
        f.write(f"> **What happened?** {summary} *The atmosphere feels {'tense' if env['stress_level'] > 0.5 else 'calm'} today with a social pressure of {env['stress_level']:.2f}.*\n\n")
        f.write(f"- P2 Position: {state['p2']} | Taxicab: {state['d_taxi']} | Euclidean: {state['d_eucl']}\n")
        
    print(f"✅ Generation {state['generation']} complete. Points drifted.")

if __name__ == "__main__":
    main()
