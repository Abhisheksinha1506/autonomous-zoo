### [⬅️ Back to Zoo Entrance](../../README.md) | [📖 Theory Index](../../docs/THEORY_INDEX.md)

---
# Hilbert Curve Filler — The Efficient Painter



## 📖 The Analogy

> Imagine a painter who wants to cover every single inch of a room without ever lifting the brush or crossing their own footsteps. This project follows a fractal path that visits every corner of the repo with perfect precision.

> **Fills repo space perfectly using a single continuous fractal path**

## 🧠 Mathematical Concept

**Space-Filling Curves**

Space-Filling Curves. A continuous curve that passes through every point of a square exactly once, demonstrating that a 1D line can perfectly fill a 2D space.

## 🎯 What This Does

Every day, the repository:
1. 1. Calculates a Hilbert path of a specific 'Order'
2. Moves the repo's 'Focus' point one step along the fractal trail
3. Tracks the current (x, y) coordinates on a virtual 16x16 grid
4. Ensures every quadrant is visited before the path resets to the beginning.
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

"A snake filling a square completely — the repo draws a path daily that touches every spot without crossing."

## 🔬 Technical Details

- **Algorithm**: Custom mathematical evolution logic
- **Parameters**: Order (Recursion level), Cell occupancy threshold
- **Safety Bounds**: Path boundary clipping, infinite loop prevention

## 📈 Evolution Log

See [history.md](history.md) for the complete evolution timeline.


## 🛠️ Technical Anatomy

- **DNA**: [evolve.py](evolve.py) (The instructions for life)
- **Vital Signs**: [state.json](state.json) (Current memory and state)
- **Evolutionary Diary**: [history.md](history.md) (Historical logs)


## 🏘️ Neighboring Organisms

⬅️ **Previous**: [fractal-music-box](../fractal-music-box/README.md)
 | ➡️ **Next**: [mandala-symmetry-generator](../mandala-symmetry-generator/README.md)

---



**Status**: 🟢 Fully Functional | **Tier**: Tier4 | **Autonomy**: ⭐⭐⭐
