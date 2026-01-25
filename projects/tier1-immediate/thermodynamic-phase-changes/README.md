### [⬅️ Back to Zoo Entrance](../../README.md) | [📖 Theory Index](../../docs/THEORY_INDEX.md)

---
# Thermodynamic Phase Changes — The Melting Ice Cube



## 📖 The Analogy

> This repo acts like water turning into ice or steam. It watches its internal temperature and decides whether its files should huddle together in a solid block or dance around like a chaotic gas.

> **Repo undergoes sudden state changes (solid/liquid/gas) at critical file counts**

## 🧠 Mathematical Concept

**Critical Phenomena**

The Ising Model. A mathematical representation of magnetism in statistical mechanics, used to study phase transitions where local interactions cause a global shift in state (solid, liquid, or gas).

## 🎯 What This Does

Every day, the repository:
1. 1. Manages a grid of 'spins' (up/down particles)
2. Calculates system energy and current temperature
3. Uses the Metropolis algorithm to flip spins and reach equilibrium
4. Detects 'Phase Transitions' when the system suddenly aligns or becomes chaotic.
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

"A crowd of people. Sometimes they stand still in a grid (solid), sometimes they run around chaotic (gas)."

## 🔬 Technical Details

- **Algorithm**: Custom mathematical evolution logic
- **Parameters**: [TODO: List parameters]
- **Safety Bounds**: [TODO: Describe limits]

## 📈 Evolution Log

See [history.md](history.md) for the complete evolution timeline.


## 🛠️ Technical Anatomy

- **DNA**: [evolve.py](evolve.py) (The instructions for life)
- **Vital Signs**: [state.json](state.json) (Current memory and state)
- **Evolutionary Diary**: [history.md](history.md) (Historical logs)


## 🏘️ Neighboring Organisms

⬅️ **Previous**: [strange-attractor-drifter](../strange-attractor-drifter/README.md)

---



**Status**: 🟢 Fully Functional | **Tier**: Tier1 | **Autonomy**: ⭐⭐⭐
