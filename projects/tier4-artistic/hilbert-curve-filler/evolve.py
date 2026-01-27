#!/usr/bin/env python3
"""
Hilbert Curve Filler
Fills repo space perfectly using a single continuous fractal path.
"""

import json
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
    env = get_social_environment()
    state["generation"] += 1
    # Move one step along the fractal path
    state["dist"] = state.get("dist", 0) + 1
    n = 2**state["order"]
    if state["dist"] >= n*n:
        state["dist"] = 0 # Loop or reset
        
    x, y = hilbert(state["dist"], n)
    state["pos"] = [x, y]
    return state


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
    print("🧬 Hilbert Curve Filler - Evolution Step")
    state = load_state()
    state = evolve_step(state)
    
    # Create human-readable summary
    summary = f"The project took another step along its infinite, space-filling path today. "
    
    summary += f"It is currently exploring the coordinate {state['pos']}, ensuring that every corner of the digital space is visited exactly once without ever crossing its own trail."

    with open("state.json", "w") as f:
        json.dump(state, f)
        
    with open("path_log.md", "a") as f:
        if state["generation"] == 1: f.write("# Fractal Traversal Log\n\n")
        f.write(f"## Generation {state['generation']}\n")
        f.write(f"> **What happened?** {summary} *The atmosphere feels {'tense' if env['stress_level'] > 0.5 else 'calm'} today with a social pressure of {env['stress_level']:.2f}.*\n\n")
        f.write(f"- Moved to {state['pos']} (Distance: {state['dist']})\n")
        
    print(f"✅ Generation {state['generation']} complete. Hilbert stepped.")

if __name__ == "__main__":
    main()
