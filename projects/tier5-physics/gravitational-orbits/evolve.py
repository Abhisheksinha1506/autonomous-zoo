#!/usr/bin/env python3
"""
Gravitational Orbits
Files orbit each other; 3-body chaotic orbits emerge (N-Body Problem).
"""

import json
import math
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








G = 0.1
DT = 0.5

def load_state():
    # 3 bodies
    defaults = {
        "generation": 0,
        "bodies": [
            {"m": 10.0, "x": 1.0, "y": 0.0, "vx": 0.0, "vy": 0.1},
            {"m": 1.0, "x": -1.0, "y": 0.0, "vx": 0.0, "vy": -0.1},
            {"m": 0.5, "x": 0.0, "y": 1.0, "vx": 0.1, "vy": 0.0}
        ],
        "history": []
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
    bodies = state["bodies"]
    
    # Calculate forces
    for i in range(len(bodies)):
        ax, ay = 0, 0
        for j in range(len(bodies)):
            if i == j: continue
            dx = bodies[j]["x"] - bodies[i]["x"]
            dy = bodies[j]["y"] - bodies[i]["y"]
            r2 = dx*dx + dy*dy + 0.1 # softening
            r = math.sqrt(r2)
            f = G * bodies[i]["m"] * bodies[j]["m"] / r2
            ax += f * dx / r / bodies[i]["m"]
            ay += f * dy / r / bodies[i]["m"]
            
        # Update velocity
        bodies[i]["vx"] += ax * DT
        bodies[i]["vy"] += ay * DT
        
    # Update position
    for b in bodies:
        b["x"] += b["vx"] * DT
        b["y"] += b["vy"] * DT
        
    return state


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
    print("🧬 Gravitational Orbits - Evolution Step")
    state = load_state()
    state = evolve_step(state)
    
    # Create human-readable summary
    summary = "Gravity pulled the repository's components closer today. "
    
    summary += f"The three digital 'bodies' glided along their chaotic orbits, demonstrating the unpredictable beauty of the N-Body problem where every mass affects every other mass."

    with open("state.json", "w") as f:
        json.dump(state, f)
        
    with open("orbit_log.md", "a") as f:
        if state["generation"] == 1: f.write("# N-Body Orbital History\n\n")
        f.write(f"## Generation {state['generation']}\n")
        f.write(f"> **What happened?** {summary} *The atmosphere feels {'tense' if env['stress_level'] > 0.5 else 'calm'} today with a social pressure of {env['stress_level']:.2f}.*\n\n")
        f.write(f"- B1 Position: ({state['bodies'][0]['x']:.2f},{state['bodies'][0]['y']:.2f})\n")
        
    print(f"✅ Generation {state['generation']} complete. Bodies glided.")

if __name__ == "__main__":
    main()
