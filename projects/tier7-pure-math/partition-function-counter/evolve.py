#!/usr/bin/env python3
"""
Partition Function Counter
Tracks integer partitions; growth mimics Hardy-Ramanujan asymptotic formula.
"""

import json
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
    env = get_social_environment()
    state["generation"] += 1
    # Increment n and calculate p(n)
    n = state["n"] + 1
    state["n"] = n
    state["count"] = partition(n)
    return state


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
    print("🧬 Partition Function Counter - Evolution Step")
    state = load_state()
    # Handle complexity growth
    if state["n"] > 50:
        print("Max depth reached. Resetting sequence.")
        state["n"] = 1
        
    state = evolve_step(state)
    
    # Create human-readable summary
    summary = f"The repository explored the theory of additive partitions today, counting the ways to build the number {state['n']}. "
    
    summary += f"The resulting count p({state['n']}) = {state['count']} adds another data point to the sequence, showing how quickly complexity grows from simple building blocks."

    with open("state.json", "w") as f:
        json.dump(state, f)
        
    with open("partitions.md", "a") as f:
        if state["generation"] == 1: f.write("# Integer Partition History\n\n")
        f.write(f"## Generation {state['generation']}\n")
        f.write(f"> **What happened?** {summary} *The atmosphere feels {'tense' if env['stress_level'] > 0.5 else 'calm'} today with a social pressure of {env['stress_level']:.2f}.*\n\n")
        f.write(f"- Count: p({state['n']}) = {state['count']}\n")
        
    print(f"✅ Generation {state['generation']} complete. p({state['n']}) counted.")

if __name__ == "__main__":
    main()
