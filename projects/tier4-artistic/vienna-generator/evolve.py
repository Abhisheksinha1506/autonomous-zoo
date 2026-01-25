#!/usr/bin/env python3
"""
Vienna Generator
Self-harmonizes musical files according to classical voice-leading rules.
"""

import json
import random
from pathlib import Path

SCALES = {
    "C_Major": [0, 2, 4, 5, 7, 9, 11],
    "G_Major": [7, 9, 11, 0, 2, 4, 6]
}

def load_state():
    defaults = {
        "generation": 0,
        "composition": [],
        "scale": "C_Major"
    }
    if Path("state.json").exists():
        with open("state.json") as f:
            try:
                state = json.load(f)
                defaults.update(state)
            except: pass
    return defaults

def evolve_step(state):
    state["generation"] += 1
    scale = SCALES[state["scale"]]
    
    # Add a new "note" (harmonized chord)
    root = random.choice(scale)
    # Simple triad: Root, Third, Fifth
    third = scale[(scale.index(root) + 2) % len(scale)]
    fifth = scale[(scale.index(root) + 4) % len(scale)]
    
    chord = [root, third, fifth]
    state["composition"].append(chord)
    
    # Keep last 16 bars
    if len(state["composition"]) > 16:
        state["composition"].pop(0)
        
    return state

def main():
    print("🧬 Vienna Generator - Evolution Step")
    state = load_state()
    state = evolve_step(state)
    with open("state.json", "w") as f:
        json.dump(state, f)
        
    with open("composition.md", "a") as f:
        if state["generation"] == 1: f.write("# Harmonized Composition Log\n\n")
        current_chord = state["composition"][-1]
        f.write(f"- Bar {state['generation']}: Chord {current_chord} in {state['scale']}\n")
        
    print(f"✅ Generation {state['generation']} complete. Music composed.")

if __name__ == "__main__":
    main()
