#!/usr/bin/env python3
"""
Fluid Dynamics Flow
Simulates laminar/turbulent flow as file creation/deletion waves (Navier-Stokes base).
"""

import json
import math
import random
from pathlib import Path

GRID_SIZE = 15

def load_state():
    defaults = {
        "generation": 0,
        "velocity_u": [[0.1 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)],
        "velocity_v": [[0.1 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)],
        "pressure": [[1.0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
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
    u = state["velocity_u"]
    v = state["velocity_v"]
    p = state["pressure"]
    
    # Simple Advection and Diffusion (Simplified)
    new_u = [row[:] for row in u]
    for i in range(1, GRID_SIZE-1):
        for j in range(1, GRID_SIZE-1):
            # Divergence check
            divergence = (u[i+1][j] - u[i-1][j] + v[i][j+1] - v[i][j-1]) / 2.0
            p[i][j] -= divergence * 0.5 # pressure adjustment
            
            # Simple advection
            new_u[i][j] = u[i][j] - (u[i][j] * divergence) + random.uniform(-0.01, 0.01)
            
    state["velocity_u"] = new_u
    return state

def render_flow(state):
    grid = state["velocity_u"]
    rows = []
    chars = " ▂▃▄▅▆▇█"
    for r in grid:
        line = ""
        for v in r:
            idx = int(abs(v) * 10) % len(chars)
            line += chars[idx]
        rows.append(line)
    return "\n".join(rows)

def main():
    print("🧬 Fluid Dynamics Flow - Evolution Step")
    state = load_state()
    state = evolve_step(state)
    
    # Create human-readable summary
    summary = "The digital fluids rippled through the repository today. "
    summary += "Using simplified Navier-Stokes logic, the project simulated laminar flow and subtle turbulence, moving 'information mass' across the digital grid."

    with open("state.json", "w") as f:
        json.dump(state, f)
        
    with open("flow_log.md", "a") as f:
        if state["generation"] == 1: f.write("# Navier-Stokes Simulation Log\n\n")
        f.write(f"## Generation {state['generation']}\n")
        f.write(f"> **What happened?** {summary}\n\n")
        f.write(f"```\n{render_flow(state)}\n```\n")
        
    print(f"✅ Generation {state['generation']} complete. Fluid flowed.")

if __name__ == "__main__":
    main()
