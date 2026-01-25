#!/usr/bin/env python3
import os
from pathlib import Path

METAPHORS = {
    # Tier 1
    "shannon-entropy-pruner": ("The Selective Librarian", "Think of this repo as a library that only keeps books with the most unique stories. If a book is just repeating what others say, the librarian 'recycles' it to make room for fresher, more interesting information."),
    "kolmogorov-compressor": ("The Master Squeezer", "This project is like a traveler trying to pack a massive suitcase into a tiny backpack without losing anything. It keeps trying different ways to fold its own code until it finds the smallest possible way to stay exactly the same."),
    "strange-attractor-drifter": ("The Digital Butterfly", "Imagine a butterfly flapping its wings in a digital forest. This project follows a chaotic trail that never crosses itself, ensuring it is always exploring a new corner of its imaginary world."),
    "reaction-diffusion-spots": ("The Chemical Zebra", "Like chemicals mixing in a laboratory or the patterns on a zebra's skin, this project creates beautiful ripples and spots by letting two 'inks' react and spread across the repository."),
    "thermodynamic-phase-changes": ("The Melting Ice Cube", "This repo acts like water turning into ice or steam. It watches its internal temperature and decides whether its files should huddle together in a solid block or dance around like a chaotic gas."),
    # Tier 2
    "collatz-conjecture-explorer": ("The Never-Ending Mountain Path", "Imagine walking a trail where you must climb every hill (odd numbers) and slide down every slope (even numbers). No matter where it starts, this project is searching for the one valley that all paths eventually lead to."),
    "penrose-tiling": ("The Infinite Floor Designer", "This project is laying tiles on an infinite floor. The catch? The pattern never repeats itself, even if you walk forever, creating a beautiful mosaic that is always unique."),
    "godel-number-encoder": ("The Universal Translator", "This project takes the entire soul of the repository and translates it into a single, incredibly long number. It's like turning a whole library into a secret code that only primes can understand."),
    "p-adic-number-line": ("The Branching Tree of Numbers", "Instead of a straight line, this project sees numbers as a vast, branching tree. It organizes its files by following these branches, where the further you go out, the 'smaller' the distance back to the center becomes."),
    "knot-polynomial-calculator": ("The Tangle Weaver", "Like a sailor working with infinite rope, this project ties and unties mathematical knots. It calculates a special 'signature' for every tangle to prove that today's knot is fundamentally different from yesterday's."),
    # Tier 3
    "prisoners-dilemma": ("The Social Conflict Simulator", "The files in this repo are like neighbors who have to decide whether to help each other or look out for themselves. They learn from each other, eventually forming groups that either trust or betray one another."),
    "small-world-networker": ("The Six Degrees of Connection", "This project acts like a socialite at a party, building shortcuts between distant files. It proves that no matter how big the repository gets, everything is only a few handshakes away."),
    "ant-colony-forager": ("The Digital Scout Ants", "A colony of digital 'ants' wanders through the folders, leaving scent trails where they find interesting information. Over time, the entire repo learns the most efficient paths to its own hidden treasures."),
    "immune-system-sentinel": ("The Repository's White Blood Cells", "This project acts like a living body's defense system. It creates a profile of what 'healthy' files look like and constantly patrols the repo to identify and eliminate any 'foreign germs' or corrupted data."),
    "resource-auction": ("The Digital Marketplace", "In this repo, space is a luxury. Files have to bid their virtual 'budgets' to occupy the most prominent spots, creating a miniature economy that evolves toward the most efficient way to spend its attention."),
    # Tier 4
    "buddhabrot-renderer": ("The Ghost in the Machine", "By tracking thousands of random digital particles that 'escape' from chaos, this project slowly reveals a ghostly, beautiful shape hidden deep inside the math, which only appears after long periods of meditation."),
    "hilbert-curve-filler": ("The Efficient Painter", "Imagine a painter who wants to cover every single inch of a room without ever lifting the brush or crossing their own footsteps. This project follows a fractal path that visits every corner of the repo with perfect precision."),
    "vienna-generator": ("The Clockwork Composer", "This repo is a self-playing piano that follows strict classical rules. Every day it writes a new bar of music, ensuring the chords perfectly harmonize with everything it has played before."),
    "fractal-music-box": ("The Echoing Melody", "A music box that plays a melody that is built into itself. Whether you listen to the whole song or zoom in on one tiny second, the rhythm remains exactly the same, repeating forever like an echo."),
    "mandala-symmetry-generator": ("The Mirror Palace", "This project treats the repo like a room full of mirrors. Every point it creates is reflected and rotated dozens of times, ensuring that the entire structure is a perfectly balanced, symmetrical mandala."),
    # Tier 5
    "fluid-dynamics-flow": ("The Digital River", "Think of this repo as a stream of water. It simulates how ripples spread and how tiny whirlpools form, moving digital weight across the folders as if they were floating on a river."),
    "gravitational-orbits": ("The Dance of the Planets", "The files in this project act like tiny planets orbiting each other. They pull and tug on one another with invisible gravity, creating a chaotic dance that changes slightly every time you look."),
    "wave-interference-patterns": ("The Ripples in a Pond", "Imagine dropping two pebbles into a digital lake. This project watches how the ripples meet, sometimes building each other up into waves and sometimes canceling each other out into stillness."),
    "thermodynamic-equilibrium": ("The Cooling Embers", "Like a fireplace after the logs have burnt down, this project slowly redistributes energy until everything is perfectly even. It is a simulation of a system finding peace and total balance."),
    "neural-net-propagation": ("The Spark of Thought", "This project acts like a tiny artificial brain. One small signal triggers a cascade of 'firing' neurons, creating a unique pattern of thought that ripples through the entire repository."),
    # Tier 6
    "error-correcting-repo": ("The Self-Healing Manuscript", "If a word in this manuscript gets smudged, it has a secret built-in code to fix itself. It's like a book that could heal its own paper if you tried to rip a page out."),
    "random-walk-organizer": ("The Wandering Archivist", "An archivist who moves files based on wherever they happen to wander that day. Eventually, the most important files end up at the 'hubs' where the archivist walks most often."),
    # Tier 7
    "partition-function-counter": ("The Brick Stacker", "How many ways can you stack a pile of bricks to reach a certain height? This project counts every single possibility, watching as the numbers explode with complexity as the pile gets taller."),
    "continued-fraction-approximants": ("The Sharp-Focus Lens", "Think of a camera lens zooming in on the number Pi. With every step, this project gets a sharper, clearer view, expressing the infinite value as a simpler and simpler fraction."),
    "galois-field-builder": ("The Closed Circle of Math", "Imagine a number system that works like a clock. If you keep adding, you just come back around. This project builds a perfectly self-contained world where the math always stays inside a single circle."),
    "zenos-paradox-divider": ("The Infinite Step-Stool", "A project that tries to reach a wall by always going half the remaining distance. It keeps getting closer and closer, forever shrinking its steps, but technically it will never quite arrive."),
    "metric-geometry": ("The Space Travelers' Map", "If you lived in a city made of blocks, you'd measure distance differently than if you could fly. This project compares these two types of travel to see how 'far' its files really are from each other.")
}

def overhaul():
    projects_processed = 0
    for tier in Path("projects").iterdir():
        if not tier.is_dir(): continue
        for project in tier.iterdir():
            if not project.is_dir(): continue
            
            readme_path = project / "README.md"
            if not readme_path.exists(): continue
            
            p_id = project.name
            if p_id not in METAPHORS:
                print(f"⚠️ Missing metaphor for {p_id}")
                continue
                
            title, description = METAPHORS[p_id]
            content = readme_path.read_text()
            
            # Professional overhaul
            # 1. Update the top heading to include the analogy
            orig_title = content.split('\n')[0].replace('# ', '').strip()
            new_header = f"# {orig_title} — {title}\n"
            
            lines = content.split('\n')
            lines[0] = new_header
            
            # 2. Inject Analogy section before Core Theory
            analogy_section = f"\n## 📖 The Analogy\n\n> {description}\n"
            
            # Find where to insert
            if "## What This Does" in content:
                # Replace the What This Does section with a more layman version
                # Or just insert before it.
                # Let's insert it before theory.
                if "## Core Theory" in content:
                    content_to_add = analogy_section + "\n## 🤖 What This Does\n\n"
                    # We'll replace the existing What This Does to keep it clean
                    # We look for the start of What This Does and the start of Theory
                    updated_content = re_replace_sections(content, title, description)
                    readme_path.write_text(updated_content)
                else:
                    # Fallback
                    lines.insert(2, analogy_section)
                    readme_path.write_text('\n'.join(lines))
            else:
                 lines.insert(2, analogy_section)
                 readme_path.write_text('\n'.join(lines))
            
            print(f"✨ {p_id}: Overhauled with analogy '{title}'")
            projects_processed += 1

    print(f"\n✅ Total projects overhauled: {projects_processed}/32")

def re_replace_sections(content, analogy_title, analogy_text):
    # Surgical replacement of the upper half of the README
    header = content.split('\n')[0]
    
    # We want to insert 📖 The Analogy after the header
    # and simplify the What This Does section.
    
    parts = content.split('## Core Theory')
    theory_half = parts[1] if len(parts) > 1 else ""
    
    new_top = f"{header}\n\n## 📖 The Analogy\n\n> **{analogy_title}**: {analogy_text}\n\n## 🤖 Layman Summary\n\nThis project is an autonomous mathematical organism. It lives inside this repository and evolves every 6 hours. Unlike traditional code, it doesn't wait for human instructions—it follows its own internal logic to grow, shift, and survive in its digital environment.\n"
    
    if theory_half:
        return new_top + "\n## 🧠 Core Theory" + theory_half
    else:
        return new_top + "\n" + "\n".join(content.split('\n')[3:])

if __name__ == "__main__":
    overhaul()
