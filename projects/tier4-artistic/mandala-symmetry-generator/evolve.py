#!/usr/bin/env python3
"""
Mandala Symmetry Generator
Arranges files into perfect rotational and reflectional symmetry groups (Dihedral Groups).
"""

import json
import math
from pathlib import Path

def load_state():
    defaults = {"generation": 0, "symmetry": 8, "points": []}
    if Path("state.json").exists():
        with open("state.json") as f:
            try:
                state = json.load(f)
                defaults.update(state)
            except: pass
    return defaults

def evolve_step(state):
    state["generation"] += 1
    sym = state["symmetry"]
    
    # Generate one "random" point in a wedge
    angle = math.radians(random.uniform(0, 360/sym))
    dist = random.uniform(0.1, 1.0)
    
    # Mirror it across the symmetry group
    new_points = []
    for i in range(sym):
        base_a = math.radians(i * (360/sym))
        px = dist * math.cos(base_a + angle)
        py = dist * math.sin(base_a + angle)
        new_points.append([round(px,3), round(py,3)])
        # Reflection
        px2 = dist * math.cos(base_a - angle)
        py2 = dist * math.sin(base_a - angle)
        new_points.append([round(px2,3), round(py2,3)])
        
    state["points"] = new_points
    return state

import random # for evolution logic

def main():
    print("🧬 Mandala Symmetry Generator - Evolution Step")
    state = load_state()
    state = evolve_step(state)
    with open("state.json", "w") as f:
        json.dump(state, f)
        
    with open("mandala.md", "a") as f:
        if state["generation"] == 1: f.write("# Dihedral Symmetry Log\n\n")
        f.write(f"- Gen {state['generation']}: Generated {len(state['points'])} points with D{state['symmetry']} symmetry.\n")
        
    print(f"✅ Generation {state['generation']} complete. Mandala symmetrical.")

if __name__ == "__main__":
    main()
