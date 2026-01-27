### [⬅️ Back to Zoo Entrance](../../README.md) | [📖 Theory Index](../../docs/THEORY_INDEX.md)

---
# Gravitational Orbits — The Dance of the Planets



### 📢 Latest Status
<!-- LATEST_STATUS_START -->
*Awaiting first evolution...*
<!-- LATEST_STATUS_END -->


## 📖 The Analogy

> The files in this project act like tiny planets orbiting each other. They pull and tug on one another with invisible gravity, creating a chaotic dance that changes slightly every time you look.

> **Files orbit each other; 3-body chaotic orbits emerge**

## 🧠 Mathematical Concept

**N-Body Problem**

The N-Body Problem. Predicts the individual motions of a group of celestial objects interacting with each other through gravitational pull.

## 🎯 What This Does

Every day, the repository:
1. 1. Places three masses with random initial velocities in the repo's space
2. Calculates the gravitational pull between every pair of masses
3. Updates the velocity and position of each 'Planet'
4. Logs the chaotic trajectories as they drift into complex orbital patterns.
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

"Planets pulling each other — files 'orbit' daily, slinging into wild paths like a solar system gone mad."

## 🔬 Technical Details

- **Algorithm**: Custom mathematical evolution logic
- **Parameters**: G (Gravitational constant), Mass range, Time step
- **Safety Bounds**: Collision detection, escape velocity boundary checks

## 📈 Evolution Log

See [history.md](history.md) for the complete evolution timeline.


## 🛠️ Technical Anatomy

- **DNA**: [evolve.py](evolve.py) (The instructions for life)
- **Vital Signs**: [state.json](state.json) (Current memory and state)
- **Evolutionary Diary**: [history.md](history.md) (Historical logs)


## 🏘️ Neighboring Organisms

⬅️ **Previous**: [fluid-dynamics-flow](../fluid-dynamics-flow/README.md)
 | ➡️ **Next**: [neural-net-propagation](../neural-net-propagation/README.md)

---



**Status**: 🟢 Fully Functional | **Tier**: Tier5 | **Autonomy**: ⭐⭐⭐