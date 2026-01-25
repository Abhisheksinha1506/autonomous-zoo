#!/usr/bin/env python3
"""
Collatz Conjecture Explorer
Walks the chaotic 3n+1 trajectories; picks new seeds when reaching 1.
"""

import json
import hashlib
import os
import random
from datetime import datetime
from pathlib import Path

# Configuration
STATE_FILE = "state.json"
HISTORY_FILE = "collatz_log.md"

def load_state():
    defaults = {
        "generation": 0,
        "current_n": 27,
        "path": [],
        "max_reached": 27,
        "explored": []
    }
    if Path(STATE_FILE).exists():
        with open(STATE_FILE) as f:
            try:
                state = json.load(f)
                defaults.update(state)
            except: pass
    return defaults

def save_state(state):
    with open(STATE_FILE, 'w') as f:
        json.dump(state, f, indent=2)

def evolve_step(state):
    state["generation"] += 1
    
    n = state["current_n"]
    state["path"].append(n)
    
    # Apply Collatz step
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1
        
    state["max_reached"] = max(state["max_reached"], n)
    state["current_n"] = n
    
    # If we reached 1, pick a new seed
    if n == 1:
        # Pick a seed based on date and generation to ensure variety
        seed_val = int(hashlib.sha256(f"{datetime.now().date()}-{state['generation']}".encode()).hexdigest(), 16)
        new_seed = (seed_val % 1000) + 2 # Avoid 1
        state["explored"].append({"seed": state["path"][0], "length": len(state["path"])})
        state["current_n"] = new_seed
        state["path"] = []
        
    return state

def render_path_viz(state):
    path = state["path"]
    if not path: return ""
    
    # Simple ASCII height map of the current path
    max_h = max(path)
    min_h = min(path)
    heights = [int((val - min_h) / (max_h - min_h + 1) * 10) for val in path]
    
    rows = []
    for h in range(10, -1, -1):
        row = "".join(["█" if ph >= h else " " for ph in heights])
        rows.append(row)
    return "\n".join(rows)

def log_history(state):
    timestamp = datetime.now().isoformat()
    n = state["current_n"]
    
    if not Path(HISTORY_FILE).exists():
        with open(HISTORY_FILE, 'w') as f:
            f.write("# Collatz Conjecture Evolution Log\n\n")

    with open(HISTORY_FILE, 'a') as f:
        f.write(f"\n## Generation {state['generation']} — {timestamp[:10]}\n\n")
        f.write(f"- **Current N**: {n}\n")
        f.write(f"- **Max Reached in Sequence**: {state['max_reached']}\n")
        f.write(f"- **Path Length**: {len(state['path'])}\n\n")
        if state["path"]:
            f.write("### Trajectory Visualization\n")
            f.write("```\n" + render_path_viz(state) + "\n```\n")

def main():
    print("🧬 Collatz Conjecture Explorer - Evolution Step")
    print("=" * 50)
    
    state = load_state()
    state = evolve_step(state)
    save_state(state)
    log_history(state)
    
    print(f"✅ Generation {state['generation']} complete. Current N: {state['current_n']}\n")

if __name__ == "__main__":
    main()
