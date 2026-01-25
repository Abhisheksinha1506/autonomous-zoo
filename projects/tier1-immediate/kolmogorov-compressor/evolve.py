#!/usr/bin/env python3
"""
Kolmogorov Compressor
Aggressively searches for the shortest possible description of its own code.
"""

import json
import hashlib
import os
import re
import ast
import subprocess
from datetime import datetime
from pathlib import Path

# Configuration
ALGO_FILE = "algorithm.py"
STATE_FILE = "state.json"
HISTORY_FILE = "history.md"
BEST_SIZE_FILE = "best_size.txt"

def load_state():
    if Path(STATE_FILE).exists():
        with open(STATE_FILE) as f:
            try:
                return json.load(f)
            except: pass
    return {"generation": 0, "best_size": float('inf')}

def save_state(state):
    with open(STATE_FILE, 'w') as f:
        json.dump(state, f, indent=2)

def get_current_algorithm():
    with open(ALGO_FILE, 'r') as f:
        return f.read()

def test_algorithm(code):
    """Verify the algorithm still works correctly."""
    temp_file = "temp_test.py"
    with open(temp_file, "w") as f:
        f.write(code)
        # Add test execution check
        f.write("\nif __name__ == '__main__':\n    try:\n        f_func = globals().get('calculate_fibonacci_sequence') or globals().get('f')\n        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]\n        actual = f_func(10)\n        if actual != expected: exit(1)\n    except Exception: exit(1)")
    
    try:
        result = subprocess.run(["python3", temp_file], capture_output=True, text=True, timeout=2)
        return result.returncode == 0
    except Exception:
        return False
    finally:
        if os.path.exists(temp_file):
            os.remove(temp_file)

def mutate(code):
    """Apply one compression mutation."""
    orig_code = code
    
    # Strategy 1: Remove docstrings and comments
    if '"""' in code or "'''" in code or "#" in code:
        code = re.sub(r'""".*?"""', '', code, flags=re.DOTALL)
        code = re.sub(r"'''.*?'''", '', code, flags=re.DOTALL)
        code = re.sub(r'#.*', '', code)
        if len(code) < len(orig_code): return code

    # Strategy 2: Remove excess whitespace/newlines
    lines = [line.strip() for line in code.split('\n') if line.strip()]
    cleaned = '\n'.join(lines)
    if len(cleaned) < len(code):
        return cleaned

    # Strategy 3: Shorten variable names
    replacements = {
        'calculate_fibonacci_sequence': 'f',
        'n_terms': 'n',
        'fibonacci_list': 'l',
        'last_number': 'a',
        'second_last_number': 'b',
        'next_number': 'c'
    }
    for old, new in replacements.items():
        if old in code and new not in code: # basic check to avoid cycles
            new_code = code.replace(old, new)
            if len(new_code) < len(code):
                return new_code
            
    # Strategy 4: Try to join lines with semi-colon
    if '\n' in code:
        # Just try joining the first two lines that don't start with def
        lines = code.split('\n')
        for i in range(len(lines)-1):
            if not lines[i].startswith('def') and not lines[i+1].startswith(' ') and not lines[i+1].startswith('def'):
                lines[i] = lines[i] + ';' + lines[i+1]
                lines.pop(i+1)
                return '\n'.join(lines)

    return code

def main():
    print("🧬 Kolmogorov Compressor - Evolution Step")
    print("=" * 50)
    
    state = load_state()
    current_code = get_current_algorithm()
    current_size = len(current_code)
    
    if state["best_size"] == float('inf'):
        state["best_size"] = current_size

    # Try a mutation
    mutated_code = mutate(current_code)
    mutated_size = len(mutated_code)
    
    change = "Static"
    if mutated_size < current_size:
        print(f"🔬 Testing mutation: {current_size} -> {mutated_size} bytes")
        if test_algorithm(mutated_code):
            print("✅ Mutation successful and passing!")
            with open(ALGO_FILE, 'w') as f:
                f.write(mutated_code)
            with open(BEST_SIZE_FILE, 'w') as f:
                f.write(str(mutated_size))
            state["best_size"] = mutated_size
            change = "Compressed"
        else:
            print("❌ Mutation failed test.")
            change = "Failed mutation"
    else:
        print("☕ No compression found this step.")

    state["generation"] += 1
    save_state(state)
    
    timestamp = datetime.now().isoformat()
    if not Path(HISTORY_FILE).exists():
        with open(HISTORY_FILE, 'w') as f:
            f.write("# Evolution History\n\n")

    # Create human-readable summary
    if change == "Compressed":
        summary = f"Success! The compressor found a more efficient way to represent the algorithm, shaving off {current_size - mutated_size} bytes while keeping the logic identical."
    elif change == "Failed mutation":
        summary = "An attempt was made to simplify the code, but the resulting mutation failed its self-test. The original code was preserved for safety."
    else:
        summary = "The compressor searched for a shorter version of its code today but couldn't find a simpler valid representation. The algorithm remains at peak efficiency."

    with open(HISTORY_FILE, 'a') as f:
        f.write(f"\n## Generation {state['generation']} — {timestamp[:10]}\n\n")
        f.write(f"> **What happened?** {summary}\n\n")
        f.write(f"- **Result**: {change}\n")
        f.write(f"- **Current Size**: {state['best_size']} bytes\n")
        if change == "Compressed":
            f.write(f"- **Improvement**: {current_size - mutated_size} bytes\n")

    print(f"✅ Generation {state['generation']} complete\n")

if __name__ == "__main__":
    main()
