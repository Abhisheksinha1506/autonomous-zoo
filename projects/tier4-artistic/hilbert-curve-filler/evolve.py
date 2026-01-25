#!/usr/bin/env python3
"""
Hilbert Curve Filler
Fills repo space perfectly using a single continuous fractal path.
"""

import json
from pathlib import Path

def hilbert(d, n):
    """Convert distance along curve to (x, y) coordinates."""
    t = d
    x, y = 0, 0
    s = 1
    while s < n:
        rx = 1 & (t // 2)
        ry = 1 & (t ^ rx)
        # Rot
        if ry == 0:
            if rx == 1:
                x = s - 1 - x
                y = s - 1 - y
            x, y = y, x
        x += s * rx
        y += s * ry
        t //= 4
        s *= 2
    return x, y

def load_state():
    defaults = {"generation": 0, "order": 4} # 16x16 grid
    if Path("state.json").exists():
        with open("state.json") as f:
            try:
                state = json.load(f)
                defaults.update(state)
            except: pass
    return defaults

def evolve_step(state):
    state["generation"] += 1
    # Move one step along the fractal path
    state["dist"] = state.get("dist", 0) + 1
    n = 2**state["order"]
    if state["dist"] >= n*n:
        state["dist"] = 0 # Loop or reset
        
    x, y = hilbert(state["dist"], n)
    state["pos"] = [x, y]
    return state

def main():
    print("🧬 Hilbert Curve Filler - Evolution Step")
    state = load_state()
    state = evolve_step(state)
    with open("state.json", "w") as f:
        json.dump(state, f)
        
    with open("path_log.md", "a") as f:
        if state["generation"] == 1: f.write("# Fractal Traversal Log\n\n")
        f.write(f"- Gen {state['generation']}: Moved to {state['pos']} (Distance: {state['dist']})\n")
        
    print(f"✅ Generation {state['generation']} complete. Hilbert stepped.")

if __name__ == "__main__":
    main()
