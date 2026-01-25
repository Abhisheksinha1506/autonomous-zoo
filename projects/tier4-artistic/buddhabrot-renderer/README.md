### [⬅️ Back to Zoo Entrance](../../README.md) | [📖 Theory Index](../../docs/THEORY_INDEX.md)

---
# Buddhabrot Renderer — The Ghost in the Machine



## 📖 The Analogy

> By tracking thousands of random digital particles that 'escape' from chaos, this project slowly reveals a ghostly, beautiful shape hidden deep inside the math, which only appears after long periods of meditation.

> **Renders the Buddha shape by plotting Mandelbrot orbit densities**

## 🧠 Mathematical Concept

**Orbit Density**

Chaos Theory & Fractal Geometry. A special rendering of the Mandelbrot set that tracks the trajectories of points which escape the fractal boundary, creating a density map.

## 🎯 What This Does

Every day, the repository:
1. 1. Picks random points in the complex plane
2. Iterates the function z = z^2 + c
3. If the point escapes to infinity, its entire path is recorded
4. Builds a density map over thousands of generations to reveal the 'Buddha' shape.
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

"Hidden Buddha in math escapes — points 'orbit' daily, filling a serene figure like a cosmic painting."

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

 | ➡️ **Next**: [fractal-music-box](../fractal-music-box/README.md)

---



**Status**: 🟢 Fully Functional | **Tier**: Tier4 | **Autonomy**: ⭐⭐⭐
