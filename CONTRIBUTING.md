# Contributing to the Autonomous Zoo

Thank you for your interest in adding new autonomous organisms to the zoo! This guide will help you create mathematically beautiful, self-evolving repositories.

## 🧬 What Makes a Good Autonomous Organism?

A great autonomous repository should:

1. **Be Truly Autonomous**: Runs daily without human intervention via GitHub Actions
2. **Have Mathematical Beauty**: Based on interesting mathematical principles
3. **Self-Modify**: Changes its own state/files based on deterministic rules
4. **Be Educational**: Teaches a concept through emergence
5. **Be Bounded**: Won't grow infinitely or crash (has safety limits)

## 📁 Required File Structure

Every project must have:

```
your-project-name/
├── README.md                    # Project documentation
├── evolve.py                    # Core evolution logic (Python 3.9+)
├── state.json                   # Current state (or similar genesis file)
├── history.md                   # Evolution log
└── .github/
    └── workflows/
        └── evolve.yml           # GitHub Action for daily automation
```

## 📝 README.md Template

```markdown
# Project Name

> One-line tagline

## 🧠 Mathematical Concept

Explain the core theory (e.g., "Shannon Entropy measures information density...")

## 🎯 What This Does

Describe the autonomous behavior in simple terms.

## 📊 Current State

- **Generation**: [tracked in state.json]
- **Status**: [current phase]

## 🚀 Running Locally

\`\`\`bash
python evolve.py  # Run one evolution step
\`\`\`

## 📖 Layman Explanation

"Imagine..."

## 🔬 Technical Details

- Algorithm used
- Parameters
- Safety bounds
```

## 🐍 evolve.py Guidelines

### Structure

```python
import json
import hashlib
from datetime import datetime
from pathlib import Path

# Constants
MAX_ITERATIONS = 1000  # Safety limit
STATE_FILE = "state.json"

def load_state():
    """Load current state from JSON"""
    if Path(STATE_FILE).exists():
        with open(STATE_FILE) as f:
            return json.load(f)
    return initialize_state()

def initialize_state():
    """Create initial state if none exists"""
    return {"generation": 0, "data": []}

def evolve_step(state):
    """
    Core evolution logic.
    
    This is where the magic happens!
    Modify state based on mathematical rules.
    """
    state["generation"] += 1
    
    # Your mathematical transformation here
    # Example: state["data"].append(compute_next_value())
    
    return state

def save_state(state):
    """Persist state to JSON"""
    with open(STATE_FILE, 'w') as f:
        json.dump(state, f, indent=2)

def log_evolution(state):
    """Append to history.md"""
    timestamp = datetime.now().isoformat()
    with open("history.md", 'a') as f:
        f.write(f"\n## Generation {state['generation']} ({timestamp})\n")
        f.write(f"- Status: {describe_state(state)}\n")

def describe_state(state):
    """Human-readable state description"""
    return f"Generation {state['generation']}"

def main():
    state = load_state()
    
    # Safety check
    if state["generation"] >= MAX_ITERATIONS:
        print("Max iterations reached. Evolution complete.")
        return
    
    state = evolve_step(state)
    save_state(state)
    log_evolution(state)
    
    print(f"✅ Evolution step {state['generation']} complete")

if __name__ == "__main__":
    main()
```

### Best Practices

- **Use deterministic randomness**: Seed with `hash(datetime.now().date())` for reproducible daily changes
- **Add safety bounds**: Prevent infinite growth (file limits, iteration caps)
- **Keep it simple**: Avoid external dependencies when possible
- **Log everything**: Write to `history.md` for transparency
- **Handle errors gracefully**: Don't crash on edge cases

## ⚙️ GitHub Action Template

```yaml
name: Daily Evolution

on:
  schedule:
    - cron: '0 0 * * *'  # Daily at midnight UTC
  workflow_dispatch:  # Allow manual triggers

jobs:
  evolve:
    runs-on: ubuntu-latest
    
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
        with:
          token: ${{ secrets.GITHUB_TOKEN }}
      
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.9'
      
      - name: Run evolution step
        run: python evolve.py
      
      - name: Commit changes
        run: |
          git config --local user.email "action@github.com"
          git config --local user.name "Autonomous Evolution Bot"
          git add .
          git diff --quiet && git diff --staged --quiet || \
            git commit -m "🧬 Evolution: Generation $(date +%Y-%m-%d)"
      
      - name: Push changes
        uses: ad-m/github-push-action@master
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          branch: main
```

## 🧪 Testing Requirements

Before submitting:

1. **Run locally 5 times**: Verify it doesn't crash
2. **Check file growth**: Ensure it won't fill disk infinitely
3. **Verify commits**: Make sure changes are meaningful
4. **Test workflow**: Use `workflow_dispatch` to trigger manually

## 📋 Submission Checklist

- [ ] All required files present
- [ ] README explains the concept clearly
- [ ] `evolve.py` has safety bounds
- [ ] Tested locally (5+ iterations)
- [ ] GitHub Action configured
- [ ] Added to main README catalog
- [ ] Layman explanation is clear

## 🎨 Choosing a Tier

- **Tier 1**: High autonomy, medium complexity, immediate impact
- **Tier 2**: Advanced math, requires deeper understanding
- **Tier 3**: Emergent behavior, game theory
- **Tier 4**: Visual/artistic output
- **Tier 5**: Physics simulations
- **Tier 6**: Computer science theory
- **Tier 7**: Pure mathematics, niche concepts

## 💡 Ideas for New Organisms

- Voronoi diagram evolution
- Prime number spirals
- Markov chain text generation
- Fourier series approximations
- Cellular automata variants
- Graph coloring algorithms
- Cryptographic hash chains

## 🤝 How to Submit

1. Fork this repository
2. Create your project in the appropriate `projects/tierN-category/` directory
3. Test thoroughly
4. Add your project to the main README catalog
5. Submit a pull request with:
   - Project name and tier
   - Brief description
   - Why it's autonomous and interesting

## ❓ Questions?

Open an issue with the `question` label, and we'll help you design your autonomous organism!

---

**Remember**: The best autonomous repositories are simple, beautiful, and teach something profound through emergence.
