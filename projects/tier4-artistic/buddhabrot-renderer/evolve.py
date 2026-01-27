#!/usr/bin/env python3
"""
Buddhabrot Renderer
Renders the "Buddha" shape by plotting Mandelbrot orbit densities.
"""

import json
import random
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








GRID_SIZE = 50
MAX_ITER = 100

def load_state():
    defaults = {
        "generation": 0,
        "density": [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
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
    grid = state["density"]
    
    # Sample points
    for _ in range(1000):
        c_re = random.uniform(-2, 1)
        c_im = random.uniform(-1.5, 1.5)
        
        # Check if point escapes
        z_re, z_im = 0, 0
        path = []
        escaped = False
        for _ in range(MAX_ITER):
            new_re = z_re*z_re - z_im*z_im + c_re
            new_im = 2*z_re*z_im + c_im
            z_re, z_im = new_re, new_im
            path.append((z_re, z_im))
            if z_re*z_re + z_im*z_im > 4:
                escaped = True
                break
        
        # Plot path of escaped points (Buddhabrot method)
        if escaped:
            for pr, pi in path:
                gx = int((pr + 2) * (GRID_SIZE - 1) / 3)
                gy = int((pi + 1.5) * (GRID_SIZE - 1) / 3)
                if 0 <= gx < GRID_SIZE and 0 <= gy < GRID_SIZE:
                    grid[gx][gy] += 1
                    
    return state

def render_ascii(state):
    grid = state["density"]
    max_val = max(max(row) for row in grid) if grid else 1
    if max_val == 0: max_val = 1
    chars = " .:-=+*#%@"
    output = []
    for row in grid:
        line = ""
        for val in row:
            idx = int((val / max_val) * (len(chars) - 1))
            line += chars[idx]
        output.append(line)
    return "\n".join(output)


def update_readme(summary):
    from pathlib import Path
    from datetime import datetime
    readme_path = Path("README.md")
    if not readme_path.exists(): return
    try:
        content = readme_path.read_text()
        start = "<!-- LATEST_STATUS_START -->"
        end = "<!-- LATEST_STATUS_END -->"
        if start not in content or end not in content: return
        parts = content.split(start)
        suffix_parts = parts[1].split(end)
        prefix = parts[0] + start
        suffix = end + suffix_parts[1]
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        new_inner = f"""
*{summary} ({timestamp})*
"""
        readme_path.write_text(prefix + new_inner + suffix)
    except Exception as e: print(f"⚠️ README Update Failed: {e}")

def main():
    env = get_social_environment()
    print("🧬 Buddhabrot Renderer - Evolution Step")
    state = load_state()
    state = evolve_step(state)
    
    # Create human-readable summary
    summary = "The repository's digital 'meditation' continue today. "
    
    summary += "By tracking the paths of points that escape the Mandelbrot set, the renderer is slowly revealing the ghostly 'Buddha' shape hidden in chaotic feedback loops."

    with open("state.json", "w") as f:
        json.dump(state, f)
        
    with open("render_log.md", "a") as f:
        if state["generation"] == 1: f.write("# Orbit Density Visualization\n\n")
        f.write(f"## Generation {state['generation']}\n")
        f.write(f"> **What happened?** {summary} *The atmosphere feels {'tense' if env['stress_level'] > 0.5 else 'calm'} today with a social pressure of {env['stress_level']:.2f}.*\n\n")
        f.write(f"```\n{render_ascii(state)}\n```\n")
        
    print(f"✅ Generation {state['generation']} complete. Buddha emerged.")

if __name__ == "__main__":
    main()
