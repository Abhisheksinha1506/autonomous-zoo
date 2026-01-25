### [⬅️ Back to Zoo Entrance](../../README.md) | [📖 Theory Index](../../docs/THEORY_INDEX.md)

---
# Resource Auction — The Digital Marketplace



## 📖 The Analogy

> In this repo, space is a luxury. Files have to bid their virtual 'budgets' to occupy the most prominent spots, creating a miniature economy that evolves toward the most efficient way to spend its attention.

> **Files bid for disk space; repo discovers Pareto-efficient allocation**

## 🧠 Mathematical Concept

**Market Equilibrium**

Vickrey-Clarke-Groves (VCG) Auctions. A mechanism for allocating resources where participants are incentivized to bid their true valuation of an item.

## 🎯 What This Does

Every day, the repository:
1. 1. Identifies 5 'Storage Slots' available in the repository
2. Collects 'Bids' from 10 competing project files
3. Allocates slots to the highest bidders
4. Updates the 'Budgets' and 'Prominence' of each file based on market outcome.
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

"Files bidding for limited 'land' — daily auctions decide who stays, like eBay for storage."

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

⬅️ **Previous**: [prisoners-dilemma](../prisoners-dilemma/README.md)
 | ➡️ **Next**: [small-world-networker](../small-world-networker/README.md)

---



**Status**: 🟢 Fully Functional | **Tier**: Tier3 | **Autonomy**: ⭐⭐⭐
