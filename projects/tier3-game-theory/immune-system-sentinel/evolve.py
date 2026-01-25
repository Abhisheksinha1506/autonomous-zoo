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
    print("🧬 Immune System Sentinel - Evolution Step")
    state = load_state()
    state = evolve_step(state)
    with open("state.json", "w") as f:
        json.dump(state, f)
        
    with open("immune_log.md", "a") as f:
        if state["generation"] == 1: f.write("# Primary Immune Response Log\n\n")
        f.write(f"- Gen {state['generation']}: {state['last_alert']} | Self Sigs: {len(state['self_signatures'])}\n")
        
    print(f"✅ Generation {state['generation']} complete. Sentinel active.")

if __name__ == "__main__":
    main()
