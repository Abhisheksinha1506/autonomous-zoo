#!/usr/bin/env python3
"""
Fractal Music Box
Generates self-similar musical compositions based on Cantor dust.
"""

import json
import hashlib
from pathlib import Path

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
    state["generation"] += 1
    # Rotate through levels or patterns
    state["pattern"] = cantor(state["generation"] % 4 + 1)
    return state

def main():
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
        f.write(f"> **What happened?** {summary}\n\n")
        viz = "".join(["█" if b else "_" for b in state["pattern"]])
        f.write(f"- Rhythm: `|{viz}|` (Level {state['generation'] % 4 + 1})\n")
        
    print(f"✅ Generation {state['generation']} complete. Fractal rhythm generated.")

if __name__ == "__main__":
    main()
