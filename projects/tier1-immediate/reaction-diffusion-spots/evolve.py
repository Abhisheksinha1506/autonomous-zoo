#!/usr/bin/env python3
"""
Reaction-Diffusion Spots
Generates "leopard-spot" or "zebra-stripe" file distributions autonomously (Gray-Scott model).
"""

import json
import hashlib
import os
import random
from datetime import datetime
from pathlib import Path

# Configuration
STATE_FILE = "state.json"
HISTORY_FILE = "patterns.md"
GRID_SIZE = 25

# Gray-Scott Parameters (tuned for "spots")
DA = 1.0
DB = 0.5
F = 0.0545
K = 0.062
DT = 1.0

def load_state():
    defaults = {
        "generation": 0,
        "grid_a": [[1.0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)],
        "grid_b": [[0.0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    }
    if Path(STATE_FILE).exists():
        with open(STATE_FILE) as f:
            try:
                state = json.load(f)
                # Filter out grid if sizes mismatch or corrupted
                if "grid_a" in state and len(state["grid_a"]) == GRID_SIZE:
                    defaults.update(state)
            except: pass
            
    # If starting fresh, add some "seeds" of B
    if defaults["generation"] == 0:
        for _ in range(5):
            cx, cy = random.randint(5, GRID_SIZE-6), random.randint(5, GRID_SIZE-6)
            for x in range(cx, cx+2):
                for y in range(cy, cy+2):
                    defaults["grid_b"][x][y] = 1.0
                    
    return defaults

def save_state(state):
    with open(STATE_FILE, 'w') as f:
        json.dump(state, f)

def laplace(grid, x, y):
    """3x3 Laplacian operator."""
    val = 0.0
    val += grid[x][y] * -1.0
    val += grid[(x-1)%GRID_SIZE][y] * 0.2
    val += grid[(x+1)%GRID_SIZE][y] * 0.2
    val += grid[x][(y-1)%GRID_SIZE] * 0.2
    val += grid[x][(y+1)%GRID_SIZE] * 0.2
    val += grid[(x-1)%GRID_SIZE][(y-1)%GRID_SIZE] * 0.05
    val += grid[(x+1)%GRID_SIZE][(y-1)%GRID_SIZE] * 0.05
    val += grid[(x-1)%GRID_SIZE][(y+1)%GRID_SIZE] * 0.05
    val += grid[(x+1)%GRID_SIZE][(y+1)%GRID_SIZE] * 0.05
    return val

def evolve_step(state):
    state["generation"] += 1
    
    a_grid = state["grid_a"]
    b_grid = state["grid_b"]
    
    new_a = [[0.0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    new_b = [[0.0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    
    # Use date to slightly jitter feed/kill rates for diversity
    seed_val = int(hashlib.sha256(str(datetime.now().date()).encode()).hexdigest(), 16)
    jitter_f = F + ((seed_val % 100) - 50) * 0.0001
    jitter_k = K + ((seed_val % 1000 // 10) - 50) * 0.0001

    # Run multiple micro-steps per day for visible change
    for _ in range(20):
        for x in range(GRID_SIZE):
            for y in range(GRID_SIZE):
                a = a_grid[x][y]
                b = b_grid[x][y]
                
                reaction = a * b * b
                la = laplace(a_grid, x, y)
                lb = laplace(b_grid, x, y)
                
                new_a[x][y] = a + (DA * la - reaction + jitter_f * (1.0 - a)) * DT
                new_b[x][y] = b + (DB * lb + reaction - (jitter_k + jitter_f) * b) * DT
                
                # Clamp
                new_a[x][y] = max(0.0, min(1.0, new_a[x][y]))
                new_b[x][y] = max(0.0, min(1.0, new_b[x][y]))
        
        a_grid = [row[:] for row in new_a]
        b_grid = [row[:] for row in new_b]

    state["grid_a"] = a_grid
    state["grid_b"] = b_grid
    return state

def render_ascii(state):
    grid_b = state["grid_b"]
    output = []
    # Map B concentration to ASCII
    chars = " .:-=+*#%@" # From low to high
    for row in grid_b:
        line = ""
        for val in row:
            idx = int(val * (len(chars) - 1))
            line += chars[idx]
        output.append(line)
    return "\n".join(output)

def log_evolution(state):
    ascii_art = render_ascii(state)
    timestamp = datetime.now().isoformat()
    
    if not Path(HISTORY_FILE).exists():
        with open(HISTORY_FILE, 'w') as f:
            f.write("# Reaction-Diffusion Evolution Log\n\n")

    with open(HISTORY_FILE, 'a') as f:
        f.write(f"\n## Generation {state['generation']} — {timestamp[:10]}\n\n")
        f.write("```\n" + ascii_art + "\n```\n")

def main():
    print("🧬 Reaction-Diffusion Spots - Evolution Step")
    print("=" * 50)
    
    state = load_state()
    state = evolve_step(state)
    save_state(state)
    log_evolution(state)
    
    print(f"✅ Generation {state['generation']} complete. Pattern evolved.\n")

if __name__ == "__main__":
    main()
