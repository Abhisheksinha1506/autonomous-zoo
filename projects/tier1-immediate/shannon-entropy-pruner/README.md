# Shannon Entropy Pruner

> **Self-cleaning repository that maximizes information density by deleting repetitive files**

## 🧠 Mathematical Concept

**Shannon Entropy** measures the average information content in a message. It's defined as:

```
H(X) = -Σ p(x) * log₂(p(x))
```

Where `p(x)` is the probability of character `x` appearing in the text.

- **High entropy** (≈8 bits/char): Random, unpredictable text (maximum information)
- **Low entropy** (≈2 bits/char): Repetitive, predictable text (minimal information)

This repository continuously prunes files with low entropy, evolving toward maximum information density.

## 🎯 What This Does

Every day, the repository:
1. Scans all files in `data/`
2. Calculates Shannon entropy for each file
3. Deletes files below the entropy threshold (4.5 bits/char)
4. If too many files are deleted, generates a new high-entropy file
5. Logs the average entropy to `entropy_history.md`

**Result**: The repo "cleans itself" like a librarian removing redundant books.

## 📊 Current State

- **Generation**: Check `state.json`
- **Average Entropy**: See `entropy_history.md`
- **Files Remaining**: Count files in `data/`

## 🚀 Running Locally

```bash
python evolve.py  # Run one evolution step
```

## 📖 Layman Explanation

"Imagine a librarian that reads the library every day and throws away any books that say the same thing. Over time, only the most unique, information-dense books remain. This repository does that with text files — it keeps only the 'surprising' ones."

## 🔬 Technical Details

- **Algorithm**: Shannon entropy calculation on character frequency
- **Threshold**: 4.5 bits/char (configurable in `evolve.py`)
- **Safety**: If all files are deleted, generates a new random file
- **Determinism**: Uses date-based seed for reproducible randomness

## 📈 Evolution Log

See [entropy_history.md](entropy_history.md) for the complete evolution timeline.

## 🎨 Visualization

```
High Entropy (Kept)  ████████░░ 8.0 bits/char
Medium Entropy       ██████░░░░ 6.0 bits/char
Low Entropy (Pruned) ███░░░░░░░ 3.0 bits/char
```

---

**Status**: 🟢 Fully Autonomous | **Tier**: 1 | **Autonomy**: ⭐⭐⭐⭐⭐
