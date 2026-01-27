#!/usr/bin/env python3
"""
Fluid Dynamics Flow
Simulates laminar/turbulent flow as file creation/deletion waves (Navier-Stokes base).
"""

import json
import math
import random
from pathlib import Path

def get_social_environment():
    """Reads global social data (Issues/PRs)."""
    try:
        env_path = Path(__file__).parent
        for _ in range(5):
            target = env_path / "social_environment.json"
            if target.exists():
                with open(target) as f: return json.load(f)
            env_path = env_path.parent
    except: pass
    return {"stress_level": 0.0, "nutrient_density": 0.0, "mutation_signature": ""}








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
    env = get_social_environment()
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


def update_readme(summary):
    readme_path = Path("README.md")
    if not readme_path.exists(): return
    with open(readme_path, 'r') as f:
        content = f.read()
    
    start_marker = "<!-- LATEST_STATUS_START -->"
    end_marker = "<!-- LATEST_STATUS_END -->"
    
    if start_marker in content and end_marker in content:
        parts = content.split(start_marker)
        prefix = parts[0] + start_marker
        suffix = end_marker + parts[1].split(end_marker)[1]
        new_content = f"{prefix}\n*{summary}*\n{suffix}"
        with open(readme_path, 'w') as f:
            f.write(new_content)

def main():
    env = get_social_environment()
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
        f.write(f"> **What happened?** {summary} *The atmosphere feels {'tense' if env['stress_level'] > 0.5 else 'calm'} today with a social pressure of {env['stress_level']:.2f}.*\n\n")
        f.write(f"```\n{render_flow(state)}\n```\n")
        
    print(f"✅ Generation {state['generation']} complete. Fluid flowed.")

if __name__ == "__main__":
    main()
