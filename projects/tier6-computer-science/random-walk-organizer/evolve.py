#!/usr/bin/env python3
"""
Random Walk Organizer
Reorganizes repo structure based on random walks and centrality (Markov Walks).
"""

import json
import random
from pathlib import Path

NODES = ["A", "B", "C", "D", "E"]

def load_state():
    defaults = {
        "generation": 0,
        "current_node": "A",
        "visits": {n: 0 for n in NODES},
        "links": {
            "A": ["B", "C"],
            "B": ["A", "D"],
            "C": ["A", "E"],
            "D": ["B"],
            "E": ["C"]
        }
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
    curr = state["current_node"]
    links = state["links"]
    
    # 1. Take 10 steps in a random walk
    for _ in range(10):
        state["visits"][curr] += 1
        curr = random.choice(links[curr])
        
    state["current_node"] = curr
    
    # 2. "Evolve" topology: connect most visited to a random node
    most_visited = max(state["visits"], key=state["visits"].get)
    target = random.choice(NODES)
    if target not in links[most_visited]:
        links[most_visited].append(target)
        state["last_link"] = f"Created hub link: {most_visited} -> {target}"
    else:
        state["last_link"] = "Static topology"
        
    return state

def main():
    print("🧬 Random Walk Organizer - Evolution Step")
    state = load_state()
    state = evolve_step(state)
    with open("state.json", "w") as f:
        json.dump(state, f)
        
    with open("centrality.md", "a") as f:
        if state["generation"] == 1: f.write("# Centrality Hub Evolution\n\n")
        f.write(f"- Gen {state['generation']}: Hub Action: {state['last_link']} | Visits: {state['visits']}\n")
        
    print(f"✅ Generation {state['generation']} complete. Hubs evolved.")

if __name__ == "__main__":
    main()
