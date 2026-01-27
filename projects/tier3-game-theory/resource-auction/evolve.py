#!/usr/bin/env python3
"""
Resource Auction
Files bid for disk space; repo discovers Pareto-efficient allocation.
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
    env = get_social_environment()
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


def update_readme(summary):
    from pathlib import Path
    from datetime import datetime
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
        new_inner = f"""
*{summary} ({timestamp})*
"""
        readme_path.write_text(prefix + new_inner + suffix)
    except Exception as e: print(f"⚠️ README Update Failed: {e}")

def main():
    env = get_social_environment()
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
        f.write(f"> **What happened?** {summary} *The atmosphere feels {'tense' if env['stress_level'] > 0.5 else 'calm'} today with a social pressure of {env['stress_level']:.2f}.*\n\n")
        f.write(f"- Winners IDs {state['winners']} | Avg Budget: {sum(p['budget'] for p in state['participants'])/len(state['participants']):.1f}\n")
        
    print(f"✅ Generation {state['generation']} complete. Auction settled.")

if __name__ == "__main__":
    main()
