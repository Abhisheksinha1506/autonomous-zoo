#!/usr/bin/env python3
"""
Metric Geometry
Explores non-Euclidean distance metrics in file organization (Taxi-cab vs L2).
"""

import json
import math
from pathlib import Path

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
    state["generation"] += 1
    # Drift the points
    state["p2"][0] += 1
    state["p2"][1] += (state["generation"] % 2)
    
    p1, p2 = state["p1"], state["p2"]
    state["d_taxi"] = taxicab(p1, p2)
    state["d_eucl"] = round(euclidean(p1, p2), 4)
    return state

def main():
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
        f.write(f"> **What happened?** {summary}\n\n")
        f.write(f"- P2 Position: {state['p2']} | Taxicab: {state['d_taxi']} | Euclidean: {state['d_eucl']}\n")
        
    print(f"✅ Generation {state['generation']} complete. Points drifted.")

if __name__ == "__main__":
    main()
