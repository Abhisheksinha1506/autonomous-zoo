#!/usr/bin/env python3
"""
Resource Auction
Files bid for disk space; repo discovers Pareto-efficient allocation.
"""

import json
import random
from pathlib import Path

NUM_SLOTS = 5

def load_state():
    defaults = {
        "generation": 0,
        "participants": [{"id": i, "budget": 100, "bid": 0} for i in range(10)],
        "winners": []
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
    
    # 1. Participants place random bids
    for p in state["participants"]:
        p["bid"] = random.randint(1, min(p["budget"], 50))
        
    # 2. Vickrey Auction (Simplified: Top N win)
    sorted_p = sorted(state["participants"], key=lambda x: x["bid"], reverse=True)
    winners = sorted_p[:NUM_SLOTS]
    
    # 3. Process outcomes
    state["winners"] = [w["id"] for w in winners]
    for p in state["participants"]:
        if p["id"] in state["winners"]:
            p["budget"] -= p["bid"]
        p["budget"] += 10 # Universal basic income for next round
        
    return state

def main():
    print("🧬 Resource Auction - Evolution Step")
    state = load_state()
    state = evolve_step(state)
    
    # Create human-readable summary
    summary = "A digital economy simulation ran today. "
    summary += f"Files bid for prominence within the repository, with winners identified as IDs {state['winners']}. The system is evolving toward a Pareto-optimal distribution of attention."

    with open("state.json", "w") as f:
        json.dump(state, f)
        
    with open("auction_log.md", "a") as f:
        if state["generation"] == 1: f.write("# Market Equilibrium Log\n\n")
        f.write(f"## Generation {state['generation']}\n")
        f.write(f"> **What happened?** {summary}\n\n")
        f.write(f"- Winners IDs {state['winners']} | Avg Budget: {sum(p['budget'] for p in state['participants'])/len(state['participants']):.1f}\n")
        
    print(f"✅ Generation {state['generation']} complete. Auction settled.")

if __name__ == "__main__":
    main()
