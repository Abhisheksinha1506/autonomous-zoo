#!/usr/bin/env python3
"""
Wave Interference Patterns
Creates standing wave patterns via constructive/destructive file interference.
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








GRID_SIZE = 20

def load_state():
    defaults = {"generation": 0}
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
    # Interference of two sources
    grid = []
    t = state["generation"] * 0.1
    for x in range(GRID_SIZE):
        row = []
        for y in range(GRID_SIZE):
            # Distances to two oscillators
            d1 = math.sqrt((x-5)**2 + (y-10)**2)
            d2 = math.sqrt((x-15)**2 + (y-10)**2)
            # Superposition
            val = math.sin(d1 - t) + math.sin(d2 - t)
            row.append(round(val, 3))
        grid.append(row)
    state["grid"] = grid
    return state

def render_ascii(state):
    grid = state["grid"]
    chars = " .:-=+*#%@"
    rows = []
    for r in grid:
        line = ""
        for v in r:
            # Map -2 to 2 into char index
            idx = int((v + 2) / 4 * (len(chars) - 1))
            line += chars[max(0, min(len(chars)-1, idx))]
        rows.append(line)
    return "\n".join(rows)


def update_readme(summary):
    readme_path = Path("README.md")
    if not readme_path.exists(): return
    with open(readme_path, 'r') as f:
        content = f.read()
    
    start_marker = "<!-- LATEST_STATUS_START -->"
    end_marker = "<!-- LATEST_STATUS_END -->"
    
    if start_marker in content and end_marker in content:
        parts = content.split(start_marker)
        prefix = parts[0] + start_marker
        suffix = end_marker + parts[1].split(end_marker)[1]
        new_content = f"{prefix}\n*{summary}*\n{suffix}"
        with open(readme_path, 'w') as f:
            f.write(new_content)

def main():
    env = get_social_environment()
    print("🧬 Wave Interference - Evolution Step")
    state = load_state()
    state = evolve_step(state)
    
    # Create human-readable summary
    summary = "Two digital oscillators vibrated through the repo's space today. "
    
    summary += "Where their signals crossed, they created patterns of reinforcement and cancellation, mimicking the way light ripples or sound waves interact in the physical world."

    with open("state.json", "w") as f:
        json.dump(state, f)
        
    with open("waves.md", "a") as f:
        if state["generation"] == 1: f.write("# Superposition Patterns\n\n")
        f.write(f"## Generation {state['generation']}\n")
        f.write(f"> **What happened?** {summary} *The atmosphere feels {'tense' if env['stress_level'] > 0.5 else 'calm'} today with a social pressure of {env['stress_level']:.2f}.*\n\n")
        f.write(f"```\n{render_ascii(state)}\n```\n")
        
    print(f"✅ Generation {state['generation']} complete. Waves interfered.")

if __name__ == "__main__":
    main()
