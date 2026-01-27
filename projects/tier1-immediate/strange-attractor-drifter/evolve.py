#!/usr/bin/env python3
"""
Strange Attractor Drifter
Files drift along chaotic butterfly-wing paths (Lorenz Attractor).
"""

import json
import hashlib
import os
from datetime import datetime
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








# Configuration
STATE_FILE = "state.json"
HISTORY_FILE = "attractor_log.md"
PLOTS_DIR = "plots"

# Lorenz Parameters
SIGMA = 10.0
RHO = 28.0
BETA = 8/3
DT = 0.01

def load_state():
    defaults = {
        "generation": 0,
        "x": 0.1,
        "y": 0.0,
        "z": 1.05,
        "points": []
    }
    if Path(STATE_FILE).exists():
        with open(STATE_FILE) as f:
            try:
                state = json.load(f)
                defaults.update(state)
            except:
                pass
    return defaults

def save_state(state):
    with open(STATE_FILE, 'w') as f:
        json.dump(state, f, indent=2)

def evolve_step(state):
    env = get_social_environment()
    """
    Apply Lorenz equations to update coordinates.
    """
    state["generation"] += 1
    
    x, y, z = state["x"], state["y"], state["z"]
    
    # Run multiple steps for better visual jump
    for _ in range(10):
        dx = SIGMA * (y - x) * DT
        dy = (x * (RHO - z) - y) * DT
        dz = (x * y - BETA * z) * DT
        
        x += dx
        y += dy
        z += dz
    
    state["x"], state["y"], state["z"] = x, y, z
    
    # Track point for history
    point = [round(x, 3), round(y, 3), round(z, 3)]
    state["points"].append(point)
    
    # Keep only last 100 points
    if len(state["points"]) > 100:
        state["points"] = state["points"][-100:]
        
    return state

def create_coordinate_file(state):
    """Create a file named by current coordinates."""
    # Clean up old coordinate files
    for f in Path('.').glob('pos_*.txt'):
        f.unlink()
        
    filename = f"pos_{state['x']:.2f}_{state['y']:.2f}_{state['z']:.2f}.txt"
    with open(filename, 'w') as f:
        f.write(f"Timestamp: {datetime.now().isoformat()}\n")
        f.write(f"Coordinates: X={state['x']:.4f}, Y={state['y']:.4f}, Z={state['z']:.4f}\n")
        f.write("Status: Drifting along the Lorenz Attractor.")

def render_ascii_plot(state):
    """Render a simple 2D projection (X-Z) of the attractor."""
    width, height = 40, 20
    grid = [[' ' for _ in range(width)] for _ in range(height)]
    
    # Bounds for Lorenz roughly: x:[-20, 20], z:[0, 50]
    points = state["points"]
    if not points: return ""
    
    for px, py, pz in points:
        gx = int((px + 20) * (width - 1) / 40)
        gz = int((pz) * (height - 1) / 50)
        
        if 0 <= gx < width and 0 <= gz < height:
            # Map Z to Y-axis of character grid (bottom up)
            grid[height - 1 - gz][gx] = '█'
            
    # Mark current position
    cx = int((state["x"] + 20) * (width - 1) / 40)
    cz = int((state["z"]) * (height - 1) / 50)
    if 0 <= cx < width and 0 <= cz < height:
        grid[height - 1 - cz][cx] = 'O'
        
    plot = '\n'.join([''.join(row) for row in grid])
    return f"```\n{plot}\n```"

def log_evolution(state):
    env = get_social_environment()
    """Update documentation with current plot."""
    plot = render_ascii_plot(state)
    timestamp = datetime.now().isoformat()
    
    # Create human-readable summary
    summary = f"Today, the project drifted through chaotic space to coordinates ({state['x']:.2f}, {state['z']:.2f}). "
    
    summary += "Like a digital butterfly, its path is determined by the famous Lorenz equations, ensuring it never follows the same trail twice."

    if not Path(HISTORY_FILE).exists():
        with open(HISTORY_FILE, 'w') as f:
            f.write("# Lorenz Attractor Evolution Log\n\n")

    with open(HISTORY_FILE, 'a') as f:
        f.write(f"\n## Generation {state['generation']} — {timestamp[:10]}\n\n")
        f.write(f"> **What happened?** {summary} *The atmosphere feels {'tense' if env['stress_level'] > 0.5 else 'calm'} today with a social pressure of {env['stress_level']:.2f}.*\n\n")
        f.write(f"Current Position: ({state['x']:.3f}, {state['y']:.3f}, {state['z']:.3f})\n\n")
        f.write("### 2D Projection (X-Z plane)\n")
        f.write(plot)
        f.write("\n")


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
    print("🧬 Strange Attractor Drifter - Evolution Step")
    print("=" * 50)
    
    state = load_state()
    state = evolve_step(state)
    create_coordinate_file(state)
    save_state(state)
    log_evolution(state)
    
    print(f"✅ Generation {state['generation']} complete at {state['x']:.2f}, {state['y']:.2f}, {state['z']:.2f}\n")

if __name__ == "__main__":
    main()
