### [⬅️ Back to Zoo Entrance](../../README.md) | [📖 Theory Index](../../docs/THEORY_INDEX.md)

---
# Prisoner's Dilemma — The Social Conflict Simulator



### 📢 Latest Status
<!-- LATEST_STATUS_START -->
*Awaiting first evolution...*
<!-- LATEST_STATUS_END -->


## 📖 The Analogy

> The files in this repo are like neighbors who have to decide whether to help each other or look out for themselves. They learn from each other, eventually forming groups that either trust or betray one another.

> **Files cooperate or defect based on neighbors; evolves Nash equilibriums**

## 🧠 Mathematical Concept

**Game Theory**

Evolutionary Game Theory. Studies how strategies (like Cooperation or Betrayal) survive in a population when the payoff depends on the actions of others.

## 🎯 What This Does

Every day, the repository:
1. 1. Populates a grid with 'Agents' having fixed strategies
2. Runs pairwise interactions where agents choose to help or betray
3. Distributes 'Points' based on a payoff matrix
4. Replaces low-scoring agents with clones of high-scoring neighbors.
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

"Two crooks deciding to snitch or stay quiet — files 'play' this game daily, learning to team up or betray."

## 🔬 Technical Details

- **Algorithm**: Custom mathematical evolution logic
- **Parameters**: Payoff matrix, Mutation rate (0.05), Imitation threshold
- **Safety Bounds**: Population size clamping, strategy drift bounds

## 📈 Evolution Log

See [history.md](history.md) for the complete evolution timeline.


## 🛠️ Technical Anatomy

- **DNA**: [evolve.py](evolve.py) (The instructions for life)
- **Vital Signs**: [state.json](state.json) (Current memory and state)
- **Evolutionary Diary**: [history.md](history.md) (Historical logs)


## 🏘️ Neighboring Organisms

⬅️ **Previous**: [immune-system-sentinel](../immune-system-sentinel/README.md)
 | ➡️ **Next**: [resource-auction](../resource-auction/README.md)

---



**Status**: 🟢 Fully Functional | **Tier**: Tier3 | **Autonomy**: ⭐⭐⭐