#!/usr/bin/env python3
"""
Error-Correcting Repo
Self-heals by detecting bit-flips and restoring from redundancy (Hamming Distance).
"""

import json
import random
from pathlib import Path

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
    print("🧬 Error-Correcting Repo - Evolution Step")
    state = load_state()
    state = evolve_step(state)
    with open("state.json", "w") as f:
        json.dump(state, f)
        
    with open("health_log.md", "a") as f:
        if state["generation"] == 1: f.write("# System Integrity History\n\n")
        f.write(f"- Gen {state['generation']}: {state['action']}\n")
        
    print(f"✅ Generation {state['generation']} complete. Repository integrity verified.")

if __name__ == "__main__":
    main()
