#!/usr/bin/env python3
"""
Thermodynamic Phase Changes
Repo undergoes sudden "state changes" (solid/liquid/gas) based on spin alignment (Ising Model).
"""

import json
import math
import hashlib
import os
import random
from datetime import datetime
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








# Configuration
STATE_FILE = "state.json"
HISTORY_FILE = "phase_log.md"
LATTICE_SIZE = 20
J = 1.0  # Coupling constant

def load_state():
    defaults = {
        "generation": 0,
        "temperature": 10.0,
        "spins": [[random.choice([-1, 1]) for _ in range(LATTICE_SIZE)] for _ in range(LATTICE_SIZE)],
        "phase": "Gas"
    }
    if Path(STATE_FILE).exists():
        with open(STATE_FILE) as f:
            try:
                state = json.load(f)
                if "spins" in state and len(state["spins"]) == LATTICE_SIZE:
                    defaults.update(state)
            except: pass
    return defaults

def save_state(state):
    with open(STATE_FILE, 'w') as f:
        json.dump(state, f)

def get_energy(spins):
    energy = 0
    for x in range(LATTICE_SIZE):
        for y in range(LATTICE_SIZE):
            s = spins[x][y]
            neighbors = spins[(x+1)%LATTICE_SIZE][y] + spins[(x-1)%LATTICE_SIZE][y] + \
                        spins[x][(y+1)%LATTICE_SIZE] + spins[x][(y-1)%LATTICE_SIZE]
            energy += -J * s * neighbors
    return energy / 2.0  # Double counted

def evolve_step(state):
    env = get_social_environment()
    state["generation"] += 1
    
    # Cooling schedule: Temperature drops over time
    # Starts at 10.0, drops to critical ~2.27, then to 0.1
    state["temperature"] = max(0.1, 10.0 * math.exp(-state["generation"] / 50.0))
    
    spins = state["spins"]
    temp = state["temperature"]
    
    # Metropolis Monte Carlo steps
    for _ in range(LATTICE_SIZE * LATTICE_SIZE * 5):
        x = random.randint(0, LATTICE_SIZE - 1)
        y = random.randint(0, LATTICE_SIZE - 1)
        
        s = spins[x][y]
        neighbors = spins[(x+1)%LATTICE_SIZE][y] + spins[(x-1)%LATTICE_SIZE][y] + \
                    spins[x][(y+1)%LATTICE_SIZE] + spins[x][(y-1)%LATTICE_SIZE]
        
        dE = 2 * J * s * neighbors
        
        if dE <= 0 or random.random() < math.exp(-dE / temp):
            spins[x][y] = -s
            
    # Determine phase based on magnetization
    mag = abs(sum(sum(row) for row in spins)) / (LATTICE_SIZE * LATTICE_SIZE)
    if temp > 4.0:
        state["phase"] = "Gas (Disordered)"
    elif temp > 2.27:
        state["phase"] = "Liquid (Fluctuating)"
    else:
        state["phase"] = "Solid (Ordered)" if mag > 0.8 else "Slush (Transition)"
        
    state["magnetization"] = round(mag, 4)
    return state

def render_ascii(state):
    rows = []
    for row in state["spins"]:
        rows.append(''.join(['█' if s == 1 else ' ' for s in row]))
    return '\n'.join(rows)

def log_evolution(state):
    env = get_social_environment()
    ascii_art = render_ascii(state)
    timestamp = datetime.now().isoformat()
    
    # Create human-readable summary
    summary = f"The repo's ambient temperature shifted to {state['temperature']:.2f}. "
    
    summary += f"The system is currently in a **{state['phase']}** state, where its internal components are {'aligning into a rigid structure' if 'Solid' in state['phase'] else 'fluctuating in a chaotic, high-energy dance'}."

    if not Path(HISTORY_FILE).exists():
        with open(HISTORY_FILE, 'w') as f:
            f.write("# Thermodynamic Phase Evolution Log\n\n")

    with open(HISTORY_FILE, 'a') as f:
        f.write(f"\n## Generation {state['generation']} — {timestamp[:10]}\n\n")
        f.write(f"> **What happened?** {summary} *The atmosphere feels {'tense' if env['stress_level'] > 0.5 else 'calm'} today with a social pressure of {env['stress_level']:.2f}.*\n\n")
        f.write(f"- **Temperature**: {state['temperature']:.3f}\n")
        f.write(f"- **Phase**: {state['phase']}\n")
        f.write(f"- **Magnetization**: {state['magnetization']}\n\n")
        f.write("```\n" + ascii_art + "\n```\n")

def main():
    env = get_social_environment()
    print("🧬 Thermodynamic Phase Changes - Evolution Step")
    print("=" * 50)
    
    state = load_state()
    state = evolve_step(state)
    save_state(state)
    log_evolution(state)
    
    print(f"✅ Generation {state['generation']} complete. State: {state['phase']}\n")

if __name__ == "__main__":
    main()
