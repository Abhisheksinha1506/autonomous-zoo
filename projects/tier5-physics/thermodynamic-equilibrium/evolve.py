#!/usr/bin/env python3
"""
Thermodynamic Equilibrium
Evolves toward "heat death" where all file interactions are uniform (Entropy maxing).
"""

import json
import random
from pathlib import Path

def load_state():
    defaults = {
        "generation": 0,
        "energy_levels": [random.randint(0, 100) for _ in range(20)],
        "entropy": 0
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
    levels = state["energy_levels"]
    
    # 2nd Law simulation: Energy redistribution (Exchange)
    # Pick two random cells and average them partially
    for _ in range(10):
        i, j = random.sample(range(len(levels)), 2)
        diff = (levels[i] - levels[j]) * 0.1
        levels[i] -= diff
        levels[j] += diff
        
    # Calculate simple variance as proxy for "order"
    avg = sum(levels) / len(levels)
    variance = sum((x - avg)**2 for x in levels) / len(levels)
    state["entropy"] = round(100 - variance, 2)
    
    return state

def main():
    print("🧬 Thermodynamic Equilibrium - Evolution Step")
    state = load_state()
    state = evolve_step(state)
    
    # Create human-readable summary
    summary = "Energy was redistributed across the repository today. "
    summary += f"Following the Second Law of Thermodynamics, the system moved closer to its final equilibrium state, with entropy increasing as variance dropped to {100-state['entropy']:.2f}."

    with open("state.json", "w") as f:
        json.dump(state, f)
        
    with open("entropy_log.md", "a") as f:
        if state["generation"] == 1: f.write("# Path to Heat Death\n\n")
        f.write(f"## Generation {state['generation']}\n")
        f.write(f"> **What happened?** {summary}\n\n")
        f.write(f"- **Current Entropy Score**: {state['entropy']}\n")
        f.write(f"- **System Variance**: {100-state['entropy']:.2f}\n")
        
    print(f"✅ Generation {state['generation']} complete. System cooled.")

if __name__ == "__main__":
    main()
