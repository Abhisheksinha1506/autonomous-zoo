#!/usr/bin/env python3
"""
Prisoner's Dilemma
Files "cooperate" or "defect" based on neighbors; evolves Nash equilibriums.
"""

import json
import random
from pathlib import Path

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

def main():
    print("🧬 Prisoner's Dilemma - Evolution Step")
    state = load_state()
    state = evolve_step(state)
    with open("state.json", "w") as f:
        json.dump(state, f)
        
    with open("game_log.md", "a") as f:
        if state["generation"] == 1: f.write("# Game Theory Evolution Log\n\n")
        f.write(f"- Gen {state['generation']}: `[{render_ascii(state)}]` | Coop Rate: {sum(1 for a in state['agents'] if a['strategy']=='C')/len(state['agents']):.2f}\n")
        
    print(f"✅ Generation {state['generation']} complete. Strategies evolved.")

if __name__ == "__main__":
    main()
