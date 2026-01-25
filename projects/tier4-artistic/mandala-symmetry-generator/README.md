### [⬅️ Back to Zoo Entrance](../../README.md) | [📖 Theory Index](../../docs/THEORY_INDEX.md)

---
# Mandala Symmetry Generator — The Mirror Palace



## 📖 The Analogy

> This project treats the repo like a room full of mirrors. Every point it creates is reflected and rotated dozens of times, ensuring that the entire structure is a perfectly balanced, symmetrical mandala.

> **Arranges files into perfect rotational and reflectional symmetry groups**

## 🧠 Mathematical Concept

**Dihedral Groups**

Group Theory (Dihedral Groups). Studies the symmetries of regular polygons, including rotations and reflections that preserve the geometric structure.

## 🎯 What This Does

Every day, the repository:
1. 1. Generates a single 'Seed Point' in a small wedge of space
2. Reflects the point across the central axis
3. Rotates the pair of points multiple times to fill a circular grid
4. Coordinates the whole group into a perfectly balanced Mandala pattern.
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

"Perfect flower symmetry — adds mirrored parts daily, building balanced designs like kaleidoscopes."

## 🔬 Technical Details

- **Algorithm**: Custom mathematical evolution logic
- **Parameters**: Rotational order n=12, Reflection toggle
- **Safety Bounds**: Coordinate symmetry validation, grid resolution cap

## 📈 Evolution Log

See [history.md](history.md) for the complete evolution timeline.


## 🛠️ Technical Anatomy

- **DNA**: [evolve.py](evolve.py) (The instructions for life)
- **Vital Signs**: [state.json](state.json) (Current memory and state)
- **Evolutionary Diary**: [history.md](history.md) (Historical logs)


## 🏘️ Neighboring Organisms

⬅️ **Previous**: [hilbert-curve-filler](../hilbert-curve-filler/README.md)
 | ➡️ **Next**: [vienna-generator](../vienna-generator/README.md)

---



**Status**: 🟢 Fully Functional | **Tier**: Tier4 | **Autonomy**: ⭐⭐⭐
