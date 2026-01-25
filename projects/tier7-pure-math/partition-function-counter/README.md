### [⬅️ Back to Zoo Entrance](../../README.md) | [📖 Theory Index](../../docs/THEORY_INDEX.md)

---
# Partition Function Counter — The Brick Stacker



## 📖 The Analogy

> How many ways can you stack a pile of bricks to reach a certain height? This project counts every single possibility, watching as the numbers explode with complexity as the pile gets taller.

> **Tracks integer partitions; growth mimics Hardy-Ramanujan asymptotic formula**

## 🧠 Mathematical Concept

**Combinatorics**

Number Theory (Integer Partitions). Counts the number of ways a positive integer n can be written as a sum of other positive integers.

## 🎯 What This Does

Every day, the repository:
1. 1. Takes the next integer in the sequence (e.g., n=1, 2, 3...)
2. Uses a recursive algorithm with memory to calculate p(n)
3. Tracks how the number of possibilities grows (Hardy-Ramanujan growth)
4. Logs each new 'Complexity Data Point' to the repository's history.
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

"Ways to split numbers — counts daily how to break integers into sums, exploding like stars."

## 🔬 Technical Details

- **Algorithm**: Custom mathematical evolution logic
- **Parameters**: Partition integer n, Memoization cache size
- **Safety Bounds**: Complexity growth alerting, integer size monitoring

## 📈 Evolution Log

See [history.md](history.md) for the complete evolution timeline.


## 🛠️ Technical Anatomy

- **DNA**: [evolve.py](evolve.py) (The instructions for life)
- **Vital Signs**: [state.json](state.json) (Current memory and state)
- **Evolutionary Diary**: [history.md](history.md) (Historical logs)


## 🏘️ Neighboring Organisms

⬅️ **Previous**: [metric-geometry](../metric-geometry/README.md)
 | ➡️ **Next**: [zenos-paradox-divider](../zenos-paradox-divider/README.md)

---



**Status**: 🟢 Fully Functional | **Tier**: Tier7 | **Autonomy**: ⭐⭐⭐
