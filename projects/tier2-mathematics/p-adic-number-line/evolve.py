#!/usr/bin/env python3
"""
P-adic Number Line
Organizes files into an "ultrametric" tree (p-adic convergence).
"""

import json
import os
from datetime import datetime
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








P = 2  # The prime base

def load_state():
    defaults = {"generation": 0, "last_val": 0}
    if Path("state.json").exists():
        with open("state.json") as f:
            try:
                state = json.load(f)
                defaults.update(state)
            except: pass
    return defaults

def get_p_adic_path(n, p):
    """Convert n to its p-adic directory path."""
    parts = []
    temp = n
    for _ in range(5): # Limit depth to 5
        parts.append(str(temp % p))
        temp //= p
    return "/".join(parts)

def evolve_step(state):
    env = get_social_environment()
    state["generation"] += 1
    
    # Generate next number in sequence
    n = state["last_val"] + state["generation"]
    state["last_val"] = n
    
    path = get_p_adic_path(n, P)
    full_path = Path("tree") / path
    full_path.mkdir(parents=True, exist_ok=True)
    
    with open(full_path / f"val_{n}.txt", "w") as f:
        f.write(f"P-adic value for n={n}, base p={P}\n")
        f.write(f"This leaf is 'close' to others in this branch under the p-adic metric.")
        
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
    print(f"🧬 P-adic Number Line (p={P}) - Evolution Step")
    state = load_state()
    state = evolve_step(state)
    
    # Create human-readable summary
    summary = f"The repo structure grew deeper into prime territory today. "
    
    summary += f"Under the p-adic metric (base {P}), the latest file was placed in a directory branch that 'converges' toward zero as the numbers get larger."

    with open("state.json", "w") as f:
        json.dump(state, f)
        
    with open("tree_viz.md", "a") as f:
        if state["generation"] == 1: f.write("# P-adic Tree Visualization\n\n")
        f.write(f"## Generation {state['generation']}\n")
        f.write(f"> **What happened?** {summary} *The atmosphere feels {'tense' if env['stress_level'] > 0.5 else 'calm'} today with a social pressure of {env['stress_level']:.2f}.*\n\n")
        f.write(f"- Added n={state['last_val']} at path `tree/{get_p_adic_path(state['last_val'], P)}`\n")
        
    print(f"✅ Generation {state['generation']} complete. Tree deepened.")

if __name__ == "__main__":
    main()
