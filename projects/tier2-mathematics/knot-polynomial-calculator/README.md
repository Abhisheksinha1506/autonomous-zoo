### [⬅️ Back to Zoo Entrance](../../README.md) | [📖 Theory Index](../../docs/THEORY_INDEX.md)

---
# Knot Polynomial Calculator — The Tangle Weaver



## 📖 The Analogy

> Like a sailor working with infinite rope, this project ties and unties mathematical knots. It calculates a special 'signature' for every tangle to prove that today's knot is fundamentally different from yesterday's.

> **Creates file structures representing quantum invariants of mathematical knots**

## 🧠 Mathematical Concept

**Topology (Jones Poly)**

Knot Theory and the Jones Polynomial. A way to distinguish different mathematical knots by calculating an algebraic polynomial that remains unchanged no matter how the knot is twisted.

## 🎯 What This Does

Every day, the repository:
1. 1. Generates a random 'Knot Diagram' (a sequence of crossings)
2. Performs R-moves (Reidemeister moves) to simplify the tangle
3. Calculates the bracket polynomial for the current configuration
4. Verifies if the knot belongs to a known family (like the trefoil or figure-eight).
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

"Determining if two tangled ropes are actually the same knot or totally different."

## 🔬 Technical Details

- **Algorithm**: Custom mathematical evolution logic
- **Parameters**: Crossing count, R-move iteration limit
- **Safety Bounds**: Self-crossing validation, polynomial complexity cap

## 📈 Evolution Log

See [history.md](history.md) for the complete evolution timeline.


## 🛠️ Technical Anatomy

- **DNA**: [evolve.py](evolve.py) (The instructions for life)
- **Vital Signs**: [state.json](state.json) (Current memory and state)
- **Evolutionary Diary**: [history.md](history.md) (Historical logs)


## 🏘️ Neighboring Organisms

⬅️ **Previous**: [godel-number-encoder](../godel-number-encoder/README.md)
 | ➡️ **Next**: [p-adic-number-line](../p-adic-number-line/README.md)

---



**Status**: 🟢 Fully Functional | **Tier**: Tier2 | **Autonomy**: ⭐⭐⭐
