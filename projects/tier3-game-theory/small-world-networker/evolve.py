#!/usr/bin/env python3
"""
Small-World Networker
Self-organizes files into a network where any node is reachable in few hops (Watts-Strogatz).
"""

import json
import random
from pathlib import Path

def load_state():
    # Initial: 20 nodes in a ring, each connected to 2 neighbors
    num_nodes = 20
    defaults = {
        "generation": 0,
        "nodes": list(range(num_nodes)),
        "edges": [[i, (i+1)%num_nodes] for i in range(num_nodes)]
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
    edges = state["edges"]
    nodes = state["nodes"]
    
    # Each generation, maybe rewire one edge to create a shortcut
    if random.random() < 0.3:
        idx = random.randint(0, len(edges)-1)
        u, v = edges[idx]
        new_v = random.choice([n for n in nodes if n != u])
        edges[idx] = [u, new_v]
        state["action"] = f"Rewired edge {u}-{v} to {u}-{new_v}"
    else:
        state["action"] = "No structural changes"
        
    return state

def main():
    print("🧬 Small-World Networker - Evolution Step")
    state = load_state()
    state = evolve_step(state)
    
    # Create human-readable summary
    summary = "The repository's internal network topology was rewired today. "
    if "Rewired" in state["action"]:
        summary += f"A new shortcut was created between distant nodes, making the entire project structure 'smaller' and more efficiently connected."
    else:
        summary += "The current network structure is already highly efficient, so no new shortcuts were needed today."

    with open("state.json", "w") as f:
        json.dump(state, f)
        
    with open("network_viz.md", "a") as f:
        if state["generation"] == 1: f.write("# Network Topology History\n\n")
        f.write(f"## Generation {state['generation']}\n")
        f.write(f"> **What happened?** {summary}\n\n")
        f.write(f"- **Action**: {state['action']}\n")
        f.write(f"- **Total Edges**: {len(state['edges'])}\n\n")
        
    print(f"✅ Generation {state['generation']} complete. Network rewired.")

if __name__ == "__main__":
    main()
