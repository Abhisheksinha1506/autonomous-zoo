#!/usr/bin/env python3
"""
Gravitational Orbits
Files orbit each other; 3-body chaotic orbits emerge (N-Body Problem).
"""

import json
import math
from pathlib import Path

G = 0.1
DT = 0.5

def load_state():
    # 3 bodies
    defaults = {
        "generation": 0,
        "bodies": [
            {"m": 10.0, "x": 1.0, "y": 0.0, "vx": 0.0, "vy": 0.1},
            {"m": 1.0, "x": -1.0, "y": 0.0, "vx": 0.0, "vy": -0.1},
            {"m": 0.5, "x": 0.0, "y": 1.0, "vx": 0.1, "vy": 0.0}
        ],
        "history": []
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
    bodies = state["bodies"]
    
    # Calculate forces
    for i in range(len(bodies)):
        ax, ay = 0, 0
        for j in range(len(bodies)):
            if i == j: continue
            dx = bodies[j]["x"] - bodies[i]["x"]
            dy = bodies[j]["y"] - bodies[i]["y"]
            r2 = dx*dx + dy*dy + 0.1 # softening
            r = math.sqrt(r2)
            f = G * bodies[i]["m"] * bodies[j]["m"] / r2
            ax += f * dx / r / bodies[i]["m"]
            ay += f * dy / r / bodies[i]["m"]
            
        # Update velocity
        bodies[i]["vx"] += ax * DT
        bodies[i]["vy"] += ay * DT
        
    # Update position
    for b in bodies:
        b["x"] += b["vx"] * DT
        b["y"] += b["vy"] * DT
        
    return state

def main():
    print("🧬 Gravitational Orbits - Evolution Step")
    state = load_state()
    state = evolve_step(state)
    with open("state.json", "w") as f:
        json.dump(state, f)
        
    with open("orbit_log.md", "a") as f:
        if state["generation"] == 1: f.write("# N-Body Orbital History\n\n")
        f.write(f"- Gen {state['generation']}: B1({state['bodies'][0]['x']:.2f},{state['bodies'][0]['y']:.2f})\n")
        
    print(f"✅ Generation {state['generation']} complete. Bodies glided.")

if __name__ == "__main__":
    main()
