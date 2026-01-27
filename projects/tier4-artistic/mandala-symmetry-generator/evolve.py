#!/usr/bin/env python3
"""
Mandala Symmetry Generator
Arranges files into perfect rotational and reflectional symmetry groups (Dihedral Groups).
"""

import json
import math
from pathlib import Path

def load_state():
    defaults = {"generation": 0, "symmetry": 8, "points": []}
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
    sym = state["symmetry"]
    
    # Generate one "random" point in a wedge
    angle = math.radians(random.uniform(0, 360/sym))
    dist = random.uniform(0.1, 1.0)
    
    # Mirror it across the symmetry group
    new_points = []
    for i in range(sym):
        base_a = math.radians(i * (360/sym))
        px = dist * math.cos(base_a + angle)
        py = dist * math.sin(base_a + angle)
        new_points.append([round(px,3), round(py,3)])
        # Reflection
        px2 = dist * math.cos(base_a - angle)
        py2 = dist * math.sin(base_a - angle)
        new_points.append([round(px2,3), round(py2,3)])
        
    state["points"] = new_points
    return state

import random # for evolution logic

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
    print("🧬 Mandala Symmetry Generator - Evolution Step")
    state = load_state()
    state = evolve_step(state)
    
    # Create human-readable summary
    summary = f"The repository's internal geometry was reflected and rotated today. "
    
    summary += f"Using D{state['symmetry']} symmetry, the generator arranged digital points into a perfect mandala, ensuring that every change on one side is echoed perfectly across the entire structure."

    with open("state.json", "w") as f:
        json.dump(state, f)
        
    with open("mandala.md", "a") as f:
        if state["generation"] == 1: f.write("# Dihedral Symmetry Log\n\n")
        f.write(f"## Generation {state['generation']}\n")
        f.write(f"> **What happened?** {summary} *The atmosphere feels {'tense' if env['stress_level'] > 0.5 else 'calm'} today with a social pressure of {env['stress_level']:.2f}.*\n\n")
        f.write(f"- Points Generated: {len(state['points'])}\n")
        f.write(f"- Symmetry Group: D{state['symmetry']}\n\n")
        
    print(f"✅ Generation {state['generation']} complete. Mandala symmetrical.")

if __name__ == "__main__":
    main()
