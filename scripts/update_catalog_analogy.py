#!/usr/bin/env python3
import os
from pathlib import Path

METAPHORS = {
    "shannon-entropy-pruner": "The Selective Librarian",
    "kolmogorov-compressor": "The Master Squeezer",
    "strange-attractor-drifter": "The Digital Butterfly",
    "reaction-diffusion-spots": "The Chemical Zebra",
    "thermodynamic-phase-changes": "The Melting Ice Cube",
    "collatz-conjecture-explorer": "The Never-Ending Mountain Path",
    "penrose-tiling": "The Infinite Floor Designer",
    "godel-number-encoder": "The Universal Translator",
    "p-adic-number-line": "The Branching Tree of Numbers",
    "knot-polynomial-calculator": "The Tangle Weaver",
    "prisoners-dilemma": "The Social Conflict Simulator",
    "small-world-networker": "The Six Degrees of Connection",
    "ant-colony-forager": "The Digital Scout Ants",
    "immune-system-sentinel": "The Repository's White Blood Cells",
    "resource-auction": "The Digital Marketplace",
    "buddhabrot-renderer": "The Ghost in the Machine",
    "hilbert-curve-filler": "The Efficient Painter",
    "vienna-generator": "The Clockwork Composer",
    "fractal-music-box": "The Echoing Melody",
    "mandala-symmetry-generator": "The Mirror Palace",
    "fluid-dynamics-flow": "The Digital River",
    "gravitational-orbits": "The Dance of the Planets",
    "wave-interference-patterns": "The Ripples in a Pond",
    "thermodynamic-equilibrium": "The Cooling Embers",
    "neural-net-propagation": "The Spark of Thought",
    "error-correcting-repo": "The Self-Healing Manuscript",
    "random-walk-organizer": "The Wandering Archivist",
    "partition-function-counter": "The Brick Stacker",
    "continued-fraction-approximants": "The Sharp-Focus Lens",
    "galois-field-builder": "The Closed Circle of Math",
    "zenos-paradox-divider": "The Infinite Step-Stool",
    "metric-geometry": "The Space Travelers' Map"
}

def update_main_readme():
    p = Path("README.md")
    if not p.exists(): return
    content = p.read_text()
    
    for p_id, analogy in METAPHORS.items():
        # Look for the table entry or list entry
        # Our main README has a table like: | [shannon-entropy-pruner](...) | ... |
        pattern = f"[{p_id}]"
        replacement = f"[{p_id} — {analogy}]"
        if pattern in content and replacement not in content:
            content = content.replace(pattern, replacement)
            
    p.write_text(content)
    print("✅ Main README updated with analogies")

if __name__ == "__main__":
    update_main_readme()
