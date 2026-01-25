#!/usr/bin/env python3
"""
Neural Net Propagation
Brain signals firing; cascading firing patterns emerge.
"""

import json
import random
from pathlib import Path

NODES = 15

def load_state():
    defaults = {
        "generation": 0,
        "activations": [0.0 for _ in range(NODES)],
        "weights": [[random.uniform(-1, 1) for _ in range(NODES)] for _ in range(NODES)]
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
    old_a = state["activations"]
    weights = state["weights"]
    
    # Stimulate a random node
    idx = random.randint(0, NODES-1)
    old_a[idx] = 1.0
    
    # Propagate
    new_a = [0.0] * NODES
    for i in range(NODES):
        total = sum(old_a[j] * weights[j][i] for j in range(NODES))
        # Sigmoid-ish activation
        new_a[i] = 1.0 / (1.0 + math.exp(-total))
        
    state["activations"] = new_a
    return state

import math # for exp

def main():
    print("🧬 Neural Net Propagation - Evolution Step")
    state = load_state()
    state = evolve_step(state)
    with open("state.json", "w") as f:
        json.dump(state, f)
        
    with open("firing_patterns.md", "a") as f:
        if state["generation"] == 1: f.write("# Neural Cascade Log\n\n")
        viz = "".join(["█" if a > 0.5 else "░" for a in state["activations"]])
        f.write(f"- Gen {state['generation']}: `[{viz}]` | Mean Activation: {sum(state['activations'])/NODES:.2f}\n")
        
    print(f"✅ Generation {state['generation']} complete. Neurons fired.")

if __name__ == "__main__":
    main()
