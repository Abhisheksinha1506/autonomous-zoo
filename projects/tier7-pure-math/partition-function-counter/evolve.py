#!/usr/bin/env python3
"""
Partition Function Counter
Tracks integer partitions; growth mimics Hardy-Ramanujan asymptotic formula.
"""

import json
from pathlib import Path

def partition(n):
    """Simple integer partition counter (Recursive with memo)."""
    memo = {}
    def count_p(n, k):
        if n == 0: return 1
        if k == 0 or n < 0: return 0
        if (n, k) in memo: return memo[(n, k)]
        res = count_p(n, k - 1) + count_p(n - k, k)
        memo[(n, k)] = res
        return res
    return count_p(n, n)

def load_state():
    defaults = {"generation": 0, "n": 1}
    if Path("state.json").exists():
        with open("state.json") as f:
            try:
                state = json.load(f)
                defaults.update(state)
            except: pass
    return defaults

def evolve_step(state):
    state["generation"] += 1
    # Increment n and calculate p(n)
    n = state["n"] + 1
    state["n"] = n
    state["count"] = partition(n)
    return state

def main():
    print("🧬 Partition Function Counter - Evolution Step")
    state = load_state()
    # Handle complexity growth
    if state["n"] > 50:
        print("Max depth reached. Resetting sequence.")
        state["n"] = 1
        
    state = evolve_step(state)
    with open("state.json", "w") as f:
        json.dump(state, f)
        
    with open("partitions.md", "a") as f:
        if state["generation"] == 1: f.write("# Integer Partition History\n\n")
        f.write(f"- Gen {state['generation']}: p({state['n']}) = {state['count']}\n")
        
    print(f"✅ Generation {state['generation']} complete. p({state['n']}) counted.")

if __name__ == "__main__":
    main()
