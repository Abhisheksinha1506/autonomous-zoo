#!/usr/bin/env python3
"""
Neural Net Propagation
Brain signals firing; cascading firing patterns emerge.
"""

import json
import random
from pathlib import Path

NODES = 15

def load_state():
    defaults = {
        "generation": 0,
        "activations": [0.0 for _ in range(NODES)],
        "weights": [[random.uniform(-1, 1) for _ in range(NODES)] for _ in range(NODES)]
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
    old_a = state["activations"]
    weights = state["weights"]
    
    # Stimulate a random node
    idx = random.randint(0, NODES-1)
    old_a[idx] = 1.0
    
    # Propagate
    new_a = [0.0] * NODES
    for i in range(NODES):
        total = sum(old_a[j] * weights[j][i] for j in range(NODES))
        # Sigmoid-ish activation
        new_a[i] = 1.0 / (1.0 + math.exp(-total))
        
    state["activations"] = new_a
    return state

import math # for exp

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
    print("🧬 Neural Net Propagation - Evolution Step")
    state = load_state()
    state = evolve_step(state)
    
    # Create human-readable summary
    summary = "A wave of digital activations rippled through the repo's synthetic brain today. "
    
    summary += f"Stimulated by a random signal, the neurons fired and propagated their charge across {NODES} connected nodes, creating a unique snapshot of computational thought."

    with open("state.json", "w") as f:
        json.dump(state, f)
        
    with open("firing_patterns.md", "a") as f:
        if state["generation"] == 1: f.write("# Neural Cascade Log\n\n")
        f.write(f"## Generation {state['generation']}\n")
        f.write(f"> **What happened?** {summary} *The atmosphere feels {'tense' if env['stress_level'] > 0.5 else 'calm'} today with a social pressure of {env['stress_level']:.2f}.*\n\n")
        viz = "".join(["█" if a > 0.5 else "░" for a in state["activations"]])
        f.write(f"- Activation Grid: `[{viz}]` | Mean: {sum(state['activations'])/NODES:.2f}\n")
        
    print(f"✅ Generation {state['generation']} complete. Neurons fired.")

if __name__ == "__main__":
    main()
