#!/usr/bin/env python3
"""
Random Walk Organizer
Reorganizes repo structure based on random walks and centrality (Markov Walks).
"""

import json
import random
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








NODES = ["A", "B", "C", "D", "E"]

def load_state():
    defaults = {
        "generation": 0,
        "current_node": "A",
        "visits": {n: 0 for n in NODES},
        "links": {
            "A": ["B", "C"],
            "B": ["A", "D"],
            "C": ["A", "E"],
            "D": ["B"],
            "E": ["C"]
        }
    }
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
    curr = state["current_node"]
    links = state["links"]
    
    # 1. Take 10 steps in a random walk
    for _ in range(10):
        state["visits"][curr] += 1
        curr = random.choice(links[curr])
        
    state["current_node"] = curr
    
    # 2. "Evolve" topology: connect most visited to a random node
    most_visited = max(state["visits"], key=state["visits"].get)
    target = random.choice(NODES)
    if target not in links[most_visited]:
        links[most_visited].append(target)
        state["last_link"] = f"Created hub link: {most_visited} -> {target}"
    else:
        state["last_link"] = "Static topology"
        
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
    print("🧬 Random Walk Organizer - Evolution Step")
    state = load_state()
    state = evolve_step(state)
    
    # Create human-readable summary
    summary = "A digital wanderer took several random steps through the repo's network today. "
    
    summary += f"By tracking which nodes were visited most often, the system identified a new 'hub' and strengthened the connection from {state['last_link'].split(':')[1] if 'hub' in state['last_link'] else 'itself'} to improve overall navigation."

    with open("state.json", "w") as f:
        json.dump(state, f)
        
    with open("centrality.md", "a") as f:
        if state["generation"] == 1: f.write("# Centrality Hub Evolution\n\n")
        f.write(f"## Generation {state['generation']}\n")
        f.write(f"> **What happened?** {summary} *The atmosphere feels {'tense' if env['stress_level'] > 0.5 else 'calm'} today with a social pressure of {env['stress_level']:.2f}.*\n\n")
        f.write(f"- Hub Action: {state['last_link']} | Visits: {state['visits']}\n")
        
    print(f"✅ Generation {state['generation']} complete. Hubs evolved.")

if __name__ == "__main__":
    main()
