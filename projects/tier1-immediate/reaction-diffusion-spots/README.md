### [⬅️ Back to Zoo Entrance](../../README.md) | [📖 Theory Index](../../docs/THEORY_INDEX.md)

---
# Reaction-Diffusion Spots — The Chemical Zebra



## 📖 The Analogy

> Like chemicals mixing in a laboratory or the patterns on a zebra's skin, this project creates beautiful ripples and spots by letting two 'inks' react and spread across the repository.

> **Generates leopard-spot or zebra-stripe file distributions autonomously**

## 🧠 Mathematical Concept

**Turing Patterns**

Gray-Scott Reaction-Diffusion Model. A mathematical model of how two chemical substances react and spread, explaining how nature creates patterns like zebra stripes or leopard spots.

## 🎯 What This Does

Every day, the repository:
1. 1. Simulates a 2D grid of two chemicals (U and V)
2. Applies 'Reaction' (V consumes U) and 'Diffusion' (chemicals spread to neighbors)
3. Renders the resulting concentrations as an ASCII pattern in the logs
4. Evolves high-concentration 'spots' over time.
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

"Two invisible chemicals mixing in a petri dish until they suddenly paint a zebra pattern."

## 🔬 Technical Details

- **Algorithm**: Custom mathematical evolution logic
- **Parameters**: Feed=0.0367, Kill=0.0649, dt=1.0
- **Safety Bounds**: Grid saturation limit, pattern stability check

## 📈 Evolution Log

See [history.md](history.md) for the complete evolution timeline.


## 🛠️ Technical Anatomy

- **DNA**: [evolve.py](evolve.py) (The instructions for life)
- **Vital Signs**: [state.json](state.json) (Current memory and state)
- **Evolutionary Diary**: [history.md](history.md) (Historical logs)


## 🏘️ Neighboring Organisms

⬅️ **Previous**: [kolmogorov-compressor](../kolmogorov-compressor/README.md)
 | ➡️ **Next**: [shannon-entropy-pruner](../shannon-entropy-pruner/README.md)

---



**Status**: 🟢 Fully Functional | **Tier**: Tier1 | **Autonomy**: ⭐⭐⭐
