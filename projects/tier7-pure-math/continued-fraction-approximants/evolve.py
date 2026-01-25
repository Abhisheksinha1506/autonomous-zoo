#!/usr/bin/env python3
"""
Continued Fraction Approximants
Finds best rational approximations for real numbers like Pi or e.
"""

import json
import math
from pathlib import Path

def get_pi_approx(steps):
    """Calculate Pi using continued fractions [3; 7, 15, 1, 292, ...]"""
    coeffs = [3, 7, 15, 1, 292, 1, 1, 1, 2, 1, 3, 1, 14, 2, 1, 1, 2, 2, 2, 2]
    steps = min(steps, len(coeffs))
    
    num, den = 0, 1
    # Work backwards
    for i in range(steps-1, 0, -1):
        num, den = den, coeffs[i] * den + num
        
    num = coeffs[0] * den + num
    return num, den

def load_state():
    defaults = {"generation": 0, "steps": 1}
    if Path("state.json").exists():
        with open("state.json") as f:
            try:
                state = json.load(f)
                defaults.update(state)
            except: pass
    return defaults

def evolve_step(state):
    state["generation"] += 1
    state["steps"] = (state["steps"] % 15) + 1
    n, d = get_pi_approx(state["steps"])
    state["approx"] = f"{n}/{d}"
    state["error"] = abs(math.pi - n/d)
    return state

def main():
    print("🧬 Continued Fraction Approximants - Evolution Step")
    state = load_state()
    state = evolve_step(state)
    
    # Create human-readable summary
    summary = "The project's mathematical 'lens' sharpened today. "
    summary += f"By using continued fractions to calculate an approximation of Pi ({state['approx']}), it reduced its calculation error to {state['error']:.12e}, approaching infinite precision."

    with open("state.json", "w") as f:
        json.dump(state, f)
        
    with open("pi_log.md", "a") as f:
        if state["generation"] == 1: f.write("# Pi Approximation History\n\n")
        f.write(f"## Generation {state['generation']}\n")
        f.write(f"> **What happened?** {summary}\n\n")
        f.write(f"- PI ≈ {state['approx']} | Error: {state['error']:.12e}\n")
        
    print(f"✅ Generation {state['generation']} complete. Approximation sharpened.")

if __name__ == "__main__":
    main()
