#!/usr/bin/env python3
"""
Ant Colony Forager
Agents leave "pheromone trails" to find optimal directory paths.
"""

import json
import random
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








GRID_SIZE = 10

def load_state():
    defaults = {
        "generation": 0,
        "pheromones": [[0.1 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)],
        "ants": [{"x": 0, "y": 0} for _ in range(5)],
        "food": {"x": GRID_SIZE-1, "y": GRID_SIZE-1}
    }
    if Path("state.json").exists():
        with open("state.json") as f:
            try:
                state = json.load(f)
                defaults.update(state)
            except: pass
    return defaults

def evolve_step(state):
    env = get_social_environment()
    state["generation"] += 1
    grid = state["pheromones"]
    ants = state["ants"]
    food = state["food"]
    
    # 1. Move ants
    for ant in ants:
        # Move biased by pheromones
        choices = []
        for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
            nx, ny = (ant["x"] + dx) % GRID_SIZE, (ant["y"] + dy) % GRID_SIZE
            choices.append(((nx, ny), grid[nx][ny]))
        
        # Simple weighted choice
        total = sum(c[1] for c in choices)
        r = random.uniform(0, total)
        curr = 0
        for pos, weight in choices:
            curr += weight
            if r <= curr:
                ant["x"], ant["y"] = pos
                break
        
        # 2. Deposit pheromone if near food
        dist = abs(ant["x"] - food["x"]) + abs(ant["y"] - food["y"])
        if dist < 2:
            grid[ant["x"]][ant["y"]] += 1.0
            
    # 3. Evaporate pheromones
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            grid[x][y] *= 0.9
            grid[x][y] = max(0.1, grid[x][y])
            
    return state

def render_grid(state):
    rows = []
    grid = state["pheromones"]
    for x in range(GRID_SIZE):
        row = ""
        for y in range(GRID_SIZE):
            v = grid[x][y]
            if v > 2.0: row += "█"
            elif v > 0.5: row += "▒"
            else: row += "░"
        rows.append(row)
    return "\n".join(rows)


def update_readme(summary):
    readme_path = Path("README.md")
    if not readme_path.exists(): return
    with open(readme_path, 'r') as f:
        content = f.read()
    
    start_marker = "<!-- LATEST_STATUS_START -->"
    end_marker = "<!-- LATEST_STATUS_END -->"
    
    if start_marker in content and end_marker in content:
        parts = content.split(start_marker)
        prefix = parts[0] + start_marker
        suffix = end_marker + parts[1].split(end_marker)[1]
        new_content = f"{prefix}\n*{summary}*\n{suffix}"
        with open(readme_path, 'w') as f:
            f.write(new_content)

def main():
    env = get_social_environment()
    print("🧬 Ant Colony Forager - Evolution Step")
    state = load_state()
    state = evolve_step(state)
    
    # Create human-readable summary
    summary = "The digital ants explored the repository's directory space today. "
    
    summary += "They strengthened pheromone trails leading toward information hubs, creating a collective memory of the most efficient paths through the project."

    with open("state.json", "w") as f:
        json.dump(state, f)
        
    with open("paths.md", "a") as f:
        if state["generation"] == 1: f.write("# Pheromone Trail Map\n\n")
        f.write(f"## Generation {state['generation']}\n")
        f.write(f"> **What happened?** {summary} *The atmosphere feels {'tense' if env['stress_level'] > 0.5 else 'calm'} today with a social pressure of {env['stress_level']:.2f}.*\n\n")
        f.write(f"```\n{render_grid(state)}\n```\n")
        
    print(f"✅ Generation {state['generation']} complete. Trails updated.")

if __name__ == "__main__":
    main()
