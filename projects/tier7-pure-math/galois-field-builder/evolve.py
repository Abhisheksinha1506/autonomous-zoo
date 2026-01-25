#!/usr/bin/env python3
"""
Galois Field Builder
Constructs algebraic closure analogs; file groups interact under modular arithmetic.
"""

import json
from pathlib import Path

P = 7 # Prime field

def load_state():
    defaults = {"generation": 0, "elements": list(range(P))}
    if Path("state.json").exists():
        with open("state.json") as f:
            try:
                state = json.load(f)
                defaults.update(state)
            except: pass
    return defaults

def evolve_step(state):
    state["generation"] += 1
    # Move to a "power" or "shift" of the field
    shift = state["generation"] % P
    state["current_op"] = f"(x + {shift}) mod {P}"
    state["result_field"] = [(x + shift) % P for x in state["elements"]]
    return state

def main():
    print(f"🧬 Galois Field GF({P}) - Evolution Step")
    state = load_state()
    state = evolve_step(state)
    
    # Create human-readable summary
    summary = f"The repo's abstract algebraic space underwent a modular transformation today. "
    summary += f"Using {state['current_op']}, the symbols in the field were shifted into a new configuration, demonstrating how finite number systems maintain consistency even when perfectly rearranged."

    with open("state.json", "w") as f:
        json.dump(state, f)
        
    with open("field_log.md", "a") as f:
        if state["generation"] == 1: f.write(f"# GF({P}) Evolution Log\n\n")
        f.write(f"## Generation {state['generation']}\n")
        f.write(f"> **What happened?** {summary}\n\n")
        f.write(f"- Operation: {state['current_op']} | Resulting Field Elements: {state['result_field']}\n")
        
    print(f"✅ Generation {state['generation']} complete. Field shifted.")

if __name__ == "__main__":
    main()
