#!/usr/bin/env python3
"""
Zeno's Paradox Divider
Files infinitely divide their content, approaching zero size asymptotically.
"""

import json
from pathlib import Path

def load_state():
    defaults = {"generation": 0, "distance": 100.0}
    if Path("state.json").exists():
        with open("state.json") as f:
            try:
                state = json.load(f)
                defaults.update(state)
            except: pass
    return defaults

def evolve_step(state):
    state["generation"] += 1
    # Each day, cut the distance in half
    state["distance"] /= 2.0
    return state

def main():
    print("🧬 Zeno's Paradox Divider - Evolution Step")
    state = load_state()
    state = evolve_step(state)
    with open("state.json", "w") as f:
        json.dump(state, f)
        
    with open("halvings.md", "a") as f:
        if state["generation"] == 1: f.write("# Infinite Division History\n\n")
        f.write(f"- Gen {state['generation']}: Distance to goal: {state['distance']:.15f}\n")
        
    print(f"✅ Generation {state['generation']} complete. Halved.")

if __name__ == "__main__":
    main()
