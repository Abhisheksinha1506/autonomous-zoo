### [⬅️ Back to Zoo Entrance](../../README.md) | [📖 Theory Index](../../docs/THEORY_INDEX.md)

---
# Metric Geometry — The Space Travelers' Map



### 📢 Latest Status
<!-- LATEST_STATUS_START -->
*Awaiting first evolution...*
<!-- LATEST_STATUS_END -->


## 📖 The Analogy

> If you lived in a city made of blocks, you'd measure distance differently than if you could fly. This project compares these two types of travel to see how 'far' its files really are from each other.

> **Explores non-Euclidean distance metrics in file organization**

## 🧠 Mathematical Concept

**Geometry**

Non-Euclidean Distance Metrics. Compares different 'Rules of Length' like the Taxicab metric (Manhattan distance) versus the standard Euclidean metric (Straight-line).

## 🎯 What This Does

Every day, the repository:
1. 1. Places two points in a coordinate grid
2. Moves one point randomly each day
3. Calculates the distance using two different 'Digital Yardsticks'
4. Shows how the definition of 'far' changes depending on the geometry of the space.
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

"A map where the distance depends on how you travel, like driving in mountains vs. flying."

## 🔬 Technical Details

- **Algorithm**: Custom mathematical evolution logic
- **Parameters**: Point coordinates, Metric type (L1, L2)
- **Safety Bounds**: Coordinate grid clamping, NaN distance protection

## 📈 Evolution Log

See [history.md](history.md) for the complete evolution timeline.


## 🛠️ Technical Anatomy

- **DNA**: [evolve.py](evolve.py) (The instructions for life)
- **Vital Signs**: [state.json](state.json) (Current memory and state)
- **Evolutionary Diary**: [history.md](history.md) (Historical logs)


## 🏘️ Neighboring Organisms

⬅️ **Previous**: [galois-field-builder](../galois-field-builder/README.md)
 | ➡️ **Next**: [partition-function-counter](../partition-function-counter/README.md)

---



**Status**: 🟢 Fully Functional | **Tier**: Tier7 | **Autonomy**: ⭐⭐⭐