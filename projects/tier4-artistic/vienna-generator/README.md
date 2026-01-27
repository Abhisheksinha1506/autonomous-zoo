### [⬅️ Back to Zoo Entrance](../../README.md) | [📖 Theory Index](../../docs/THEORY_INDEX.md)

---
# Vienna Generator — The Clockwork Composer



### 📢 Latest Status
<!-- LATEST_STATUS_START -->
*Awaiting first evolution...*
<!-- LATEST_STATUS_END -->


## 📖 The Analogy

> This repo is a self-playing piano that follows strict classical rules. Every day it writes a new bar of music, ensuring the chords perfectly harmonize with everything it has played before.

> **Self-harmonizes musical files according to classical voice-leading rules**

## 🧠 Mathematical Concept

**Voice Leading**

Music Theory & Voice Leading. Implements classical rules for chord progression and harmony, ensuring mathematical balance in musical intervals.

## 🎯 What This Does

Every day, the repository:
1. 1. Selects a musical scale (e.g., C Major)
2. Generates a 'Triad' (three-note chord) based on the current position
3. Applies voice-leading rules to pick the next chord smoothly
4. Records the composition bar-by-bar to build a multi-generation symphony.
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

"Notes leading to harmony — the repo composes music daily that 'flows' smoothly, like an AI Bach."

## 🔬 Technical Details

- **Algorithm**: Custom mathematical evolution logic
- **Parameters**: Scale type, Chord weightings, Harmonic friction
- **Safety Bounds**: Voice-leading constraint validation, range clamping

## 📈 Evolution Log

See [history.md](history.md) for the complete evolution timeline.


## 🛠️ Technical Anatomy

- **DNA**: [evolve.py](evolve.py) (The instructions for life)
- **Vital Signs**: [state.json](state.json) (Current memory and state)
- **Evolutionary Diary**: [history.md](history.md) (Historical logs)


## 🏘️ Neighboring Organisms

⬅️ **Previous**: [mandala-symmetry-generator](../mandala-symmetry-generator/README.md)

---



**Status**: 🟢 Fully Functional | **Tier**: Tier4 | **Autonomy**: ⭐⭐⭐