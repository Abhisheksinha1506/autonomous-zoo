#!/usr/bin/env python3
"""
Wave Interference Patterns
Creates standing wave patterns via constructive/destructive file interference.
"""

import json
import math
from pathlib import Path

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

def main():
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
        f.write(f"> **What happened?** {summary}\n\n")
        f.write(f"```\n{render_ascii(state)}\n```\n")
        
    print(f"✅ Generation {state['generation']} complete. Waves interfered.")

if __name__ == "__main__":
    main()
