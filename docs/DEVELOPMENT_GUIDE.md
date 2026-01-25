# Development Guide

## Creating a New Autonomous Organism

This guide walks you through creating a new self-evolving repository from scratch.

## Step 1: Choose Your Mathematical Concept

Pick a concept that:
- Has clear, deterministic rules
- Produces interesting emergent behavior
- Can be bounded (won't grow infinitely)
- Is educational or beautiful

**Examples**: Fractals, number sequences, graph algorithms, physics simulations, game theory

## Step 2: Design the Evolution Logic

Ask yourself:
1. **What is the state?** (What data persists between runs?)
2. **What is the transformation?** (How does state change each day?)
3. **What is the output?** (What files/logs are created?)
4. **What are the bounds?** (When does it stop or reset?)

## Step 3: Create the Directory Structure

```bash
mkdir -p my-project/{.github/workflows}
cd my-project
```

## Step 4: Write the README

Use this template:

```markdown
# Project Name

> One-line description

## 🧠 Mathematical Concept

Explain the theory...

## 🎯 What This Does

Describe daily behavior...

## 📖 Layman Explanation

"Imagine..."
```

## Step 5: Implement `evolve.py`

### Minimal Template

```python
#!/usr/bin/env python3
import json
from pathlib import Path

STATE_FILE = "state.json"

def load_state():
    if Path(STATE_FILE).exists():
        with open(STATE_FILE) as f:
            return json.load(f)
    return {"generation": 0}

def save_state(state):
    with open(STATE_FILE, 'w') as f:
        json.dump(state, f, indent=2)

def evolve_step(state):
    state["generation"] += 1
    # Your logic here
    return state

def main():
    state = load_state()
    state = evolve_step(state)
    save_state(state)
    print(f"✅ Generation {state['generation']}")

if __name__ == "__main__":
    main()
```

### Best Practices

1. **Use date-based seeds** for deterministic randomness:
```python
import hashlib
from datetime import datetime

seed = int(hashlib.sha256(str(datetime.now().date()).encode()).hexdigest(), 16)
```

2. **Add safety bounds**:
```python
if state["generation"] >= 1000:
    print("Max iterations reached")
    return
```

3. **Log everything**:
```python
with open("history.md", 'a') as f:
    f.write(f"## Gen {state['generation']}: {description}\\n")
```

## Step 6: Create the GitHub Action

`.github/workflows/evolve.yml`:

```yaml
name: Daily Evolution

on:
  schedule:
    - cron: '0 0 * * *'
  workflow_dispatch:

jobs:
  evolve:
    runs-on: ubuntu-latest
    permissions:
      contents: write
    
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      
      - name: Run evolution
        run: python evolve.py
      
      - name: Commit changes
        run: |
          git config --local user.email "action@github.com"
          git config --local user.name "Evolution Bot"
          git add .
          git diff --quiet && git diff --staged --quiet || \\
            git commit -m "🧬 Evolution: $(date +%Y-%m-%d)"
      
      - name: Push changes
        uses: ad-m/github-push-action@master
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
```

## Step 7: Test Locally

```bash
# Run 5 times to verify it works
for i in {1..5}; do
    python evolve.py
    echo "---"
done

# Check output
cat state.json
cat history.md
```

## Step 8: Initialize State Files

```bash
echo '{"generation": 0}' > state.json
echo "# Evolution History" > history.md
```

## Step 9: Deploy to GitHub

```bash
git init
git add .
git commit -m "Initial commit: Autonomous organism"
git branch -M main
git remote add origin https://github.com/username/my-project.git
git push -u origin main
```

## Step 10: Enable GitHub Actions

1. Go to repository Settings → Actions → General
2. Set "Workflow permissions" to "Read and write permissions"
3. Save

## Example Projects by Complexity

### Beginner: Counter
```python
def evolve_step(state):
    state["count"] = state.get("count", 0) + 1
    return state
```

### Intermediate: Fibonacci
```python
def evolve_step(state):
    a = state.get("a", 0)
    b = state.get("b", 1)
    state["a"], state["b"] = b, a + b
    return state
```

### Advanced: Cellular Automaton
```python
def evolve_step(state):
    grid = state.get("grid", [[0]*10 for _ in range(10)])
    new_grid = apply_rules(grid)  # Conway's Game of Life
    state["grid"] = new_grid
    return state
```

## Debugging Tips

### Evolution Not Running?
- Check GitHub Actions tab for errors
- Verify workflow permissions
- Test `evolve.py` locally first

### Files Not Committing?
- Ensure `git add .` includes all changed files
- Check that files actually changed (diff not empty)

### Infinite Growth?
- Add file count limits
- Use rolling windows (keep last N files)
- Implement compression

## Advanced Techniques

### Visualization

Create ASCII art in markdown:
```python
def render_grid(grid):
    return '\\n'.join(''.join('█' if cell else '░' for cell in row) for row in grid)
```

### Multi-file Evolution

```python
for i in range(10):
    Path(f"data/file_{i}.txt").write_text(generate_content(i))
```

### Deterministic Randomness

```python
import random
random.seed(get_date_seed())
value = random.randint(1, 100)
```

## Publishing Your Organism

1. Add to Autonomous Zoo (submit PR)
2. Tag with appropriate tier
3. Include layman explanation
4. Document the mathematical concept

---

**Happy evolving! 🧬**
