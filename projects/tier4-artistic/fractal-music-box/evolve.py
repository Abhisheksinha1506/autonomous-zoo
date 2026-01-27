#!/usr/bin/env python3
"""
Fractal Music Box
Generates self-similar musical compositions based on Cantor dust.
"""

import json
import hashlib
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








def cantor(n):
    """Generate Cantor set indices."""
    if n == 0: return [True]
    prev = cantor(n-1)
    # Middle third is False
    return prev + [False] * len(prev) + prev

def load_state():
    defaults = {"generation": 0, "level": 3}
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
    # Rotate through levels or patterns
    state["pattern"] = cantor(state["generation"] % 4 + 1)
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
    print("🧬 Fractal Music Box - Evolution Step")
    state = load_state()
    state = evolve_step(state)
    
    # Create human-readable summary
    summary = "A self-similar rhythm was generated today using Cantor dust. "
    
    summary += f"The melody is composed of repeating patterns that look identical whether you zoom in or zoom out, creating a recursive musical structure."

    with open("state.json", "w") as f:
        json.dump(state, f)
        
    with open("fractal_score.md", "a") as f:
        if state["generation"] == 1: f.write("# Cantor Set Melodies\n\n")
        f.write(f"## Generation {state['generation']}\n")
        f.write(f"> **What happened?** {summary} *The atmosphere feels {'tense' if env['stress_level'] > 0.5 else 'calm'} today with a social pressure of {env['stress_level']:.2f}.*\n\n")
        viz = "".join(["█" if b else "_" for b in state["pattern"]])
        f.write(f"- Rhythm: `|{viz}|` (Level {state['generation'] % 4 + 1})\n")
        
    print(f"✅ Generation {state['generation']} complete. Fractal rhythm generated.")

if __name__ == "__main__":
    main()
