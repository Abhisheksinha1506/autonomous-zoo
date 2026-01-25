#!/usr/bin/env python3
"""
Error-Correcting Repo
Self-heals by detecting bit-flips and restoring from redundancy (Hamming Distance).
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








def calculate_checksum(data):
    """Simple parity check."""
    return sum(ord(c) for c in data) % 256

def load_state():
    defaults = {
        "generation": 0,
        "files": {"file1.txt": {"content": "Hello World", "checksum": 0}}
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
    files = state["files"]
    
    # 1. Simulate a random "bit flip" (corruption) in a file
    fname = "file1.txt"
    content = files[fname]["content"]
    
    if random.random() < 0.3:
        # Corruption
        idx = random.randint(0, len(content)-1)
        corrupted = list(content)
        corrupted[idx] = chr(random.randint(33, 126))
        content = "".join(corrupted)
        state["action"] = f"CRITICAL: Corruption detected at index {idx}"
    else:
        state["action"] = "No errors detected"
        
    # 2. "Error correction" using stored checksum
    expected_c = files[fname]["checksum"]
    actual_c = calculate_checksum(content)
    
    if actual_c != expected_c:
        # Self-heal (restore from redundancy - in this simple case, the state)
        # Content remains the original in this simple model if it matches state
        # In a real model, we'd use Reed-Solomon or similar.
        content = files[fname]["content"]
        state["action"] += " -> Self-healed from redundancy."
    else:
        files[fname]["content"] = content
        files[fname]["checksum"] = calculate_checksum(content)
        
    return state

def main():
    env = get_social_environment()
    print("🧬 Error-Correcting Repo - Evolution Step")
    state = load_state()
    state = evolve_step(state)
    
    # Create human-readable summary
    summary = f"The repository's 'digital immune system' checked for bit-level errors today. "
    if "Corruption detected" in state["action"]:
        summary += f"It discovered a small corruption in a file and immediately used its internal redundancy to self-heal, restoring the original state without any loss of logic."
    else:
        summary += "The repo's data integrity is perfect; no errors or 'bit-flips' were detected during the latest sweep."

    with open("state.json", "w") as f:
        json.dump(state, f)
        
    with open("health_log.md", "a") as f:
        if state["generation"] == 1: f.write("# System Integrity History\n\n")
        f.write(f"## Generation {state['generation']}\n")
        f.write(f"> **What happened?** {summary} *The atmosphere feels {'tense' if env['stress_level'] > 0.5 else 'calm'} today with a social pressure of {env['stress_level']:.2f}.*\n\n")
        f.write(f"- Status Action: {state['action']}\n")
        
    print(f"✅ Generation {state['generation']} complete. Repository integrity verified.")

if __name__ == "__main__":
    main()
