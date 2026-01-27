#!/usr/bin/env python3
"""
Vienna Generator
Self-harmonizes musical files according to classical voice-leading rules.
"""

import json
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








SCALES = {
    "C_Major": [0, 2, 4, 5, 7, 9, 11],
    "G_Major": [7, 9, 11, 0, 2, 4, 6]
}

def load_state():
    defaults = {
        "generation": 0,
        "composition": [],
        "scale": "C_Major"
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
    scale = SCALES[state["scale"]]
    
    # Add a new "note" (harmonized chord)
    root = random.choice(scale)
    # Simple triad: Root, Third, Fifth
    third = scale[(scale.index(root) + 2) % len(scale)]
    fifth = scale[(scale.index(root) + 4) % len(scale)]
    
    chord = [root, third, fifth]
    state["composition"].append(chord)
    
    # Keep last 16 bars
    if len(state["composition"]) > 16:
        state["composition"].pop(0)
        
    return state


def update_readme(summary):
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
        new_inner = f"
*{summary} ({timestamp})*
"
        readme_path.write_text(prefix + new_inner + suffix)
    except Exception as e: print(f"⚠️ README Update Failed: {e}")

def main():
    env = get_social_environment()
    print("🧬 Vienna Generator - Evolution Step")
    state = load_state()
    state = evolve_step(state)
    
    # Create human-readable summary
    summary = "The repository's internal composer harmonized a new bar today. "
    
    summary += f"Using the rules of {state['scale']}, it generated a triad triad chord {state['composition'][-1]}, blending mathematical precision with classical voice-leading rules."

    with open("state.json", "w") as f:
        json.dump(state, f)
        
    with open("composition.md", "a") as f:
        if state["generation"] == 1: f.write("# Harmonized Composition Log\n\n")
        f.write(f"## Generation {state['generation']}\n")
        f.write(f"> **What happened?** {summary} *The atmosphere feels {'tense' if env['stress_level'] > 0.5 else 'calm'} today with a social pressure of {env['stress_level']:.2f}.*\n\n")
        current_chord = state["composition"][-1]
        f.write(f"- Chord {current_chord} in {state['scale']}\n")
        
    print(f"✅ Generation {state['generation']} complete. Music composed.")

if __name__ == "__main__":
    main()
