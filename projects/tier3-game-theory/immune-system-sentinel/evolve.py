#!/usr/bin/env python3
"""
Immune System Sentinel
Detects "anomalous" files and eliminates them; maintains "self" definition.
"""

import json
import hashlib
import os
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








def load_state():
    defaults = {
        "generation": 0,
        "self_signatures": [],
        "antibodies": []
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
    
    # 1. Learn current files as 'self' if not present
    files = list(Path('.').glob('*.py')) + list(Path('.').glob('*.md'))
    for f in files:
        sig = hashlib.md5(f.name.encode()).hexdigest()[:8]
        if sig not in state["self_signatures"]:
            state["self_signatures"].append(sig)
            
    # 2. Simulate detection of a random "virus" (new file)
    if random.random() < 0.2:
        v_name = f"virus_{random.randint(100,999)}.tmp"
        with open(v_name, 'w') as f: f.write("malicious content")
        state["last_alert"] = f"Detected and eliminated {v_name}"
        os.remove(v_name)
    else:
        state["last_alert"] = "System clear"
        
    return state

def main():
    env = get_social_environment()
    print("🧬 Immune System Sentinel - Evolution Step")
    state = load_state()
    state = evolve_step(state)
    
    # Create human-readable summary
    summary = f"The sentinel performed a deep scan of the repo's 'DNA' today. "
    if "eliminated" in state["last_alert"]:
        summary += f"It discovered a foreign file signature and successfully eliminated it to preserve the repository's structural integrity."
    else:
        summary += "The system is healthy; no anomalies or 'infections' were detected during the latest sweep."

    with open("state.json", "w") as f:
        json.dump(state, f)
        
    with open("immune_log.md", "a") as f:
        if state["generation"] == 1: f.write("# Primary Immune Response Log\n\n")
        f.write(f"## Generation {state['generation']}\n")
        f.write(f"> **What happened?** {summary} *The atmosphere feels {'tense' if env['stress_level'] > 0.5 else 'calm'} today with a social pressure of {env['stress_level']:.2f}.*\n\n")
        f.write(f"- **Sentinel Status**: {state['last_alert']}\n")
        f.write(f"- **Self-Signatures**: {len(state['self_signatures'])}\n\n")
        
    print(f"✅ Generation {state['generation']} complete. Sentinel active.")

if __name__ == "__main__":
    main()
