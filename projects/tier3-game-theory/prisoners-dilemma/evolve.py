#!/usr/bin/env python3
"""
Prisoner's Dilemma
Files "cooperate" or "defect" based on neighbors; evolves Nash equilibriums.
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








# Payoff Matrix (Row vs Column)
# (C,C): 3,3 | (C,D): 0,5 | (D,C): 5,0 | (D,D): 1,1
PAYOFFS = {
    ('C', 'C'): 3,
    ('C', 'D'): 0,
    ('D', 'C'): 5,
    ('D', 'D'): 1
}

def load_state():
    defaults = {
        "generation": 0,
        "agents": [{'strategy': random.choice(['C', 'D']), 'score': 0} for _ in range(20)]
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
    agents = state["agents"]
    num = len(agents)
    
    # Each agent plays against its two neighbors
    new_scores = [0] * num
    for i in range(num):
        me = agents[i]['strategy']
        left = agents[(i-1)%num]['strategy']
        right = agents[(i+1)%num]['strategy']
        
        new_scores[i] = PAYOFFS[(me, left)] + PAYOFFS[(me, right)]
        
    # Update strategies: Copy better neighbor (Imitation)
    new_agents = []
    for i in range(num):
        best_neighbor = i
        if new_scores[(i-1)%num] > new_scores[i]:
            best_neighbor = (i-1)%num
        if new_scores[(i+1)%num] > new_scores[best_neighbor]:
            best_neighbor = (i+1)%num
            
        new_strat = agents[best_neighbor]['strategy']
        
        # Occasional mutation
        if random.random() < 0.05:
            new_strat = 'C' if new_strat == 'D' else 'D'
            
        new_agents.append({'strategy': new_strat, 'score': new_scores[i]})
        
    state["agents"] = new_agents
    return state

def render_ascii(state):
    return "".join(['█' if a['strategy'] == 'C' else '░' for a in state["agents"]])


def update_readme(summary):
    readme_path = Path("README.md")
    if not readme_path.exists(): return
    try:
        content = readme_path.read_text()
        start = "<!-- LATEST_STATUS_START -->"
        end = "<!-- LATEST_STATUS_END -->"
        if start not in content or end not in content: return
        parts = content.split(start)
        suffix_parts = parts[1].split(end)
        prefix = parts[0] + start
        suffix = end + suffix_parts[1]
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        new_inner = f"
*{summary} ({timestamp})*
"
        readme_path.write_text(prefix + new_inner + suffix)
    except Exception as e: print(f"⚠️ README Update Failed: {e}")

def main():
    env = get_social_environment()
    print("🧬 Prisoner's Dilemma - Evolution Step")
    state = load_state()
    state = evolve_step(state)
    
    # Create human-readable summary
    coop_rate = sum(1 for a in state['agents'] if a['strategy']=='C')/len(state['agents'])
    summary = f"A round of game theory interactions was played across the repo. "
    if coop_rate > 0.7:
        summary += "Altruism is thriving today! Most files are choosing to cooperate with their neighbors."
    elif coop_rate < 0.3:
        summary += "Betrayal is rampant! The system is drifting toward a cynical Nash equilibrium of mutual defection."
    else:
        summary += "The repo is in a complex state of social tension, with cooperation and betrayal balancing each other out."

    with open("state.json", "w") as f:
        json.dump(state, f)
        
    with open("game_log.md", "a") as f:
        if state["generation"] == 1: f.write("# Game Theory Evolution Log\n\n")
        f.write(f"## Generation {state['generation']} — {coop_rate*100:.1f}% Coop\n")
        f.write(f"> **What happened?** {summary} *The atmosphere feels {'tense' if env['stress_level'] > 0.5 else 'calm'} today with a social pressure of {env['stress_level']:.2f}.*\n\n")
        f.write(f"- Grid State: `[{render_ascii(state)}]`\n\n")
        
    print(f"✅ Generation {state['generation']} complete. Strategies evolved.")

if __name__ == "__main__":
    main()
