### [⬅️ Back to Zoo Entrance](../../README.md) | [📖 Theory Index](../../docs/THEORY_INDEX.md)

---
# Fluid Dynamics Flow — The Digital River



## 📖 The Analogy

> Think of this repo as a stream of water. It simulates how ripples spread and how tiny whirlpools form, moving digital weight across the folders as if they were floating on a river.

> **Simulates laminar/turbulent flow as file creation/deletion waves**

## 🧠 Mathematical Concept

**Navier-Stokes**

Navier-Stokes Equations. The fundamental equations of fluid mechanics that describe how the velocity, pressure, and temperature of a moving fluid are related.

## 🎯 What This Does

Every day, the repository:
1. 1. Operates on a 15x15 grid of 'Velocity' and 'Pressure'
2. Applies 'Advection' (carrying properties with the flow)
3. Calculates 'Divergence' to ensure the fluid is incompressible
4. Renders the resulting ripples and whirlpools as an ASCII flow field.
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

"Water swirling in a pipe — files 'flow' daily, creating smooth or chaotic waves, like simulating rivers."

## 🔬 Technical Details

- **Algorithm**: Custom mathematical evolution logic
- **Parameters**: Viscosity, Diffusion rate, Time step
- **Safety Bounds**: Divergence-free pressure check, velocity clamping

## 📈 Evolution Log

See [history.md](history.md) for the complete evolution timeline.


## 🛠️ Technical Anatomy

- **DNA**: [evolve.py](evolve.py) (The instructions for life)
- **Vital Signs**: [state.json](state.json) (Current memory and state)
- **Evolutionary Diary**: [history.md](history.md) (Historical logs)


## 🏘️ Neighboring Organisms

 | ➡️ **Next**: [gravitational-orbits](../gravitational-orbits/README.md)

---



**Status**: 🟢 Fully Functional | **Tier**: Tier5 | **Autonomy**: ⭐⭐⭐
