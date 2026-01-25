### [⬅️ Back to Zoo Entrance](../../README.md) | [📖 Theory Index](../../docs/THEORY_INDEX.md)

---
# Strange Attractor Drifter — The Digital Butterfly



## 📖 The Analogy

> Imagine a butterfly flapping its wings in a digital forest. This project follows a chaotic trail that never crosses itself, ensuring it is always exploring a new corner of its imaginary world.

> **Files drift along butterfly-wing paths; sensitive to initial conditions**

## 🧠 Mathematical Concept

**Chaos Theory (Lorenz)**

The Lorenz System. A set of differential equations describing atmospheric convection, famous for the 'butterfly effect' where small changes in initial conditions lead to vastly different outcomes.

## 🎯 What This Does

Every day, the repository:
1. 1. Calculates current (x, y, z) coordinates from `state.json`
2. Solves the Lorenz equations using a small time step (dt)
3. Updates the trajectory vector and creates a new coordinate file
4. Appends the new point to the visual history.
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

"A weather simulation where moving a butterfly one wing changes the path of a hurricane a week later."

## 🔬 Technical Details

- **Algorithm**: Custom mathematical evolution logic
- **Parameters**: Sigma=10.0, Rho=28.0, Beta=2.667
- **Safety Bounds**: Coordinates bounded to [-50, 50], State normalization

## 📈 Evolution Log

See [history.md](history.md) for the complete evolution timeline.


## 🛠️ Technical Anatomy

- **DNA**: [evolve.py](evolve.py) (The instructions for life)
- **Vital Signs**: [state.json](state.json) (Current memory and state)
- **Evolutionary Diary**: [history.md](history.md) (Historical logs)


## 🏘️ Neighboring Organisms

⬅️ **Previous**: [shannon-entropy-pruner](../shannon-entropy-pruner/README.md)
 | ➡️ **Next**: [thermodynamic-phase-changes](../thermodynamic-phase-changes/README.md)

---



**Status**: 🟢 Fully Functional | **Tier**: Tier1 | **Autonomy**: ⭐⭐⭐
