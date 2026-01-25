### [⬅️ Back to Zoo Entrance](../../README.md) | [📖 Theory Index](../../docs/THEORY_INDEX.md)

---
# Continued Fraction Approximants — The Sharp-Focus Lens



## 📖 The Analogy

> Think of a camera lens zooming in on the number Pi. With every step, this project gets a sharper, clearer view, expressing the infinite value as a simpler and simpler fraction.

> **Finds best rational approximations for real numbers like π or e**

## 🧠 Mathematical Concept

**Diophantine Approx**

Continued Fractions. An infinite sequence of integers used to represent real numbers (like Pi or e) with increasing precision as more terms are added.

## 🎯 What This Does

Every day, the repository:
1. 1. Starts with the first term of the continued fraction for Pi (3)
2. Adds a new term from the sequence in each generation
3. Calculates the resulting 'Sharpest Fraction' for that level of focus
4. Measures the 'Calculation Error' to show the closing gap toward infinity.
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

"Best fractions for pi — refines daily, getting closer like honing a blade."

## 🔬 Technical Details

- **Algorithm**: Custom mathematical evolution logic
- **Parameters**: Sequence depth, Error tolerance
- **Safety Bounds**: Denominator growth monitoring, floating point precision limits

## 📈 Evolution Log

See [history.md](history.md) for the complete evolution timeline.


## 🛠️ Technical Anatomy

- **DNA**: [evolve.py](evolve.py) (The instructions for life)
- **Vital Signs**: [state.json](state.json) (Current memory and state)
- **Evolutionary Diary**: [history.md](history.md) (Historical logs)


## 🏘️ Neighboring Organisms

 | ➡️ **Next**: [galois-field-builder](../galois-field-builder/README.md)

---



**Status**: 🟢 Fully Functional | **Tier**: Tier7 | **Autonomy**: ⭐⭐⭐
