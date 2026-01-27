#!/usr/bin/env python3
"""
Shannon Entropy Pruner
Autonomous repository that maximizes information density
"""

import json
import math
import os
import random
import hashlib
from datetime import datetime
from pathlib import Path
from collections import Counter

def get_social_environment():
    """Reads global social data (Issues/PRs)."""
    try:
        env_path = Path(__file__).parent
        for _ in range(5):
            target = env_path / "social_environment.json"
            if target.exists():
                with open(target) as f: return json.load(f)
            env_path = env_path.parent
    except: pass
    return {"stress_level": 0.0, "nutrient_density": 0.0, "mutation_signature": ""}








# Configuration
DATA_DIR = "data"
STATE_FILE = "state.json"
HISTORY_FILE = "entropy_history.md"
ENTROPY_THRESHOLD = 4.5  # bits per character
MIN_FILES = 5  # Keep at least this many files
MAX_FILES = 50  # Safety limit

def calculate_entropy(text):
    """
    Calculate Shannon entropy of text in bits per character.
    
    H(X) = -Σ p(x) * log₂(p(x))
    """
    if not text:
        return 0.0
    
    # Count character frequencies
    counter = Counter(text)
    length = len(text)
    
    # Calculate entropy
    entropy = 0.0
    for count in counter.values():
        probability = count / length
        if probability > 0:
            entropy -= probability * math.log2(probability)
    
    return entropy

def load_state():
    """Load current state from JSON"""
    if Path(STATE_FILE).exists():
        with open(STATE_FILE) as f:
            return json.load(f)
    return {
        "generation": 0,
        "total_files_pruned": 0,
        "average_entropy": 0.0
    }

def save_state(state):
    """Persist state to JSON"""
    with open(STATE_FILE, 'w') as f:
        json.dump(state, f, indent=2)

def get_date_seed():
    """Generate deterministic seed from current date"""
    date_str = str(datetime.now().date())
    return int(hashlib.sha256(date_str.encode()).hexdigest(), 16) % (2**32)

def generate_random_file(filename):
    """Generate a high-entropy random file"""
    random.seed(get_date_seed())
    
    # Mix of random words and characters for high entropy
    words = ['quantum', 'entropy', 'chaos', 'fractal', 'prime', 'fibonacci', 
             'mandelbrot', 'lorenz', 'turing', 'godel', 'cantor', 'hilbert']
    
    content_parts = []
    for _ in range(random.randint(50, 200)):
        if random.random() < 0.7:
            content_parts.append(random.choice(words))
        else:
            content_parts.append(chr(random.randint(33, 126)))
        content_parts.append(' ' if random.random() < 0.3 else '')
    
    content = ''.join(content_parts)
    
    with open(filename, 'w') as f:
        f.write(content)
    
    return content

def initialize_data_dir():
    """Create initial data files if directory is empty"""
    Path(DATA_DIR).mkdir(exist_ok=True)
    
    files = list(Path(DATA_DIR).glob('*.txt'))
    if len(files) < MIN_FILES:
        print(f"📁 Initializing data directory with {MIN_FILES} files...")
        for i in range(MIN_FILES):
            generate_random_file(f"{DATA_DIR}/file_{i:03d}.txt")

def evolve_step(state):
    env = get_social_environment()
    """
    Core evolution logic:
    1. Calculate entropy for all files
    2. Prune low-entropy files
    3. Generate new file if needed
    """
    state["generation"] += 1
    
    # Ensure data directory exists
    initialize_data_dir()
    
    # Scan all files and calculate entropy
    file_entropies = []
    for filepath in Path(DATA_DIR).glob('*.txt'):
        try:
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            entropy = calculate_entropy(content)
            file_entropies.append({
                'path': filepath,
                'entropy': entropy,
                'size': len(content)
            })
        except Exception as e:
            print(f"⚠️  Error reading {filepath}: {e}")
    
    if not file_entropies:
        print("📁 No files found, initializing...")
        initialize_data_dir()
        return state
    
    # Calculate statistics
    avg_entropy = sum(f['entropy'] for f in file_entropies) / len(file_entropies)
    state["average_entropy"] = round(avg_entropy, 3)
    
    # Prune low-entropy files (but keep minimum)
    files_to_prune = [
        f for f in file_entropies 
        if f['entropy'] < ENTROPY_THRESHOLD
    ]
    
    current_file_count = len(file_entropies)
    files_pruned = 0
    
    for file_info in files_to_prune:
        if current_file_count - files_pruned > MIN_FILES:
            print(f"🗑️  Pruning {file_info['path'].name} (entropy: {file_info['entropy']:.2f})")
            file_info['path'].unlink()
            files_pruned += 1
            state["total_files_pruned"] += 1
    
    # If we pruned files, maybe generate a new high-entropy one
    random.seed(get_date_seed())
    if files_pruned > 0 and random.random() < 0.3:
        new_filename = f"{DATA_DIR}/gen_{state['generation']:04d}.txt"
        content = generate_random_file(new_filename)
        new_entropy = calculate_entropy(content)
        print(f"✨ Generated {Path(new_filename).name} (entropy: {new_entropy:.2f})")
    
    print(f"📊 Average entropy: {avg_entropy:.3f} bits/char")
    print(f"📁 Files remaining: {current_file_count - files_pruned}")
    
    return state

def log_evolution(state):
    env = get_social_environment()
    """Append to history.md"""
    timestamp = datetime.now().isoformat()
    
    # Create history file if it doesn't exist
    if not Path(HISTORY_FILE).exists():
        with open(HISTORY_FILE, 'w') as f:
            f.write("# Entropy Evolution History\n\n")
            f.write("Tracking the journey toward maximum information density.\n\n")
    
    file_count = len(list(Path(DATA_DIR).glob('*.txt')))
    
    # Create human-readable summary
    total_pruned = state.get('total_files_pruned', 0)
    summary = f"The pruner scanned {file_count + total_pruned} files today. "
    if total_pruned > 0:
        summary += f"It discovered and 'recycled' some repetitive files to keep the repo's information density ultra-high."
    else:
        summary += "All current files contain dense, high-quality information, so no cleanup was required."

    with open(HISTORY_FILE, 'a') as f:
        f.write(f"\n## Generation {state['generation']} — {timestamp[:10]}\n\n")
        f.write(f"> **What happened?** {summary} *The atmosphere feels {'tense' if env['stress_level'] > 0.5 else 'calm'} today with a social pressure of {env['stress_level']:.2f}.*\n\n")
        f.write(f"- **Average Entropy**: {state.get('average_entropy', 0):.3f} bits/char\n")
        f.write(f"- **Files Remaining**: {file_count}\n")
        f.write(f"- **Total Pruned**: {total_pruned}\n")
        
        # Visual bar
        bar_length = int(state['average_entropy'] * 10)
        bar = '█' * bar_length + '░' * (80 - bar_length)
        f.write(f"- **Density**: `{bar[:40]}`\n")


def update_readme(summary):
    from pathlib import Path
    from datetime import datetime
    readme_path = Path("README.md")
    if not readme_path.exists(): return
    try:
        content = readme_path.read_text()
        start = "<!-- LATEST_STATUS_START -->"
        end = "<!-- LATEST_STATUS_END -->"
        if start not in content or end not in content: return
        parts = content.split(start)
        suffix_parts = parts[1].split(end)
        prefix = parts[0] + start
        suffix = end + suffix_parts[1]
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        new_inner = f"""
*{summary} ({timestamp})*
"""
        readme_path.write_text(prefix + new_inner + suffix)
    except Exception as e: print(f"⚠️ README Update Failed: {e}")

def main():
    env = get_social_environment()
    """Main evolution loop"""
    print("🧬 Shannon Entropy Pruner - Evolution Step")
    print("=" * 50)
    
    state = load_state()
    
    # Safety check
    if state["generation"] >= 1000:
        print("⚠️  Max generations reached. Evolution complete.")
        return
    
    state = evolve_step(state)
    save_state(state)
    log_evolution(state)
    
    print("=" * 50)
    print(f"✅ Generation {state['generation']} complete\n")

if __name__ == "__main__":
    main()
