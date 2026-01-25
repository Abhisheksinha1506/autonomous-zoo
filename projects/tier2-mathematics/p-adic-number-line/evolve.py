#!/usr/bin/env python3
"""
P-adic Number Line
Organizes files into an "ultrametric" tree (p-adic convergence).
"""

import json
import os
from datetime import datetime
from pathlib import Path

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

def main():
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
        f.write(f"> **What happened?** {summary}\n\n")
        f.write(f"- Added n={state['last_val']} at path `tree/{get_p_adic_path(state['last_val'], P)}`\n")
        
    print(f"✅ Generation {state['generation']} complete. Tree deepened.")

if __name__ == "__main__":
    main()
