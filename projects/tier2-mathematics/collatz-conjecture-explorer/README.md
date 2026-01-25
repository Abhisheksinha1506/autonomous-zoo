### [⬅️ Back to Zoo Entrance](../../README.md) | [📖 Theory Index](../../docs/THEORY_INDEX.md)

---
# Collatz Conjecture Explorer — The Never-Ending Mountain Path



## 📖 The Analogy

> Imagine walking a trail where you must climb every hill (odd numbers) and slide down every slope (even numbers). No matter where it starts, this project is searching for the one valley that all paths eventually lead to.

> **Walks the chaotic 3n+1 trajectories; picks new seeds when reaching 1**

## 🧠 Mathematical Concept

**Number Theory**

The 3n + 1 Problem. A sequence where if n is even, divide by 2; if n is odd, multiply by 3 and add 1. The conjecture states that every positive integer eventually reaches 1.

## 🎯 What This Does

Every day, the repository:
1. 1. Takes the current number from `state.json`
2. Applies the Collatz rules (x/2 or 3x+1)
3. Tracks the maximum value reached during the trajectory
4. When it reaches 1, it picks a new 'seed' to start a fresh exploration.
2. Every generation, the project updates its `state.json` file with the latest calculation, preserving the chain of life across GitHub Action cycles.
3. Logs progress to `history.md` every 6 hours (staggered schedule)

## 📊 Current State

- **Generation**: Check `state.json`
- **Status**: See `history.md`

## 🚀 Running Locally

```bash
python evolve.py  # Run one evolution step
```

## 📖 Layman Explanation

"A game where if the number is even you cut it in half, if odd you triple it. Does it always hit 1?"

## 🔬 Technical Details

- **Algorithm**: Custom mathematical evolution logic
- **Parameters**: Seed range [2, 1000], Maximum step count
- **Safety Bounds**: Auto-reset on reaching 1, cycle detection bounds

## 📈 Evolution Log

See [history.md](history.md) for the complete evolution timeline.


## 🛠️ Technical Anatomy

- **DNA**: [evolve.py](evolve.py) (The instructions for life)
- **Vital Signs**: [state.json](state.json) (Current memory and state)
- **Evolutionary Diary**: [history.md](history.md) (Historical logs)


## 🏘️ Neighboring Organisms

 | ➡️ **Next**: [godel-number-encoder](../godel-number-encoder/README.md)

---



**Status**: 🟢 Fully Functional | **Tier**: Tier2 | **Autonomy**: ⭐⭐⭐
