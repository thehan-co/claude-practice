import random

# ANSI color codes
COLORS = [
    "\033[91m",  # Red
    "\033[92m",  # Green
    "\033[94m",  # Blue
]
RESET = "\033[0m"

DICE_FACES = {
    1: [
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"
    ],
    2: [
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"
    ],
    3: [
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"
    ],
    4: [
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"
    ],
    5: [
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"
    ],
    6: [
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘"
    ]
}

def roll_dice(num_dice=1):
    """Roll dice and return results."""
    rolls = [random.randint(1, 6) for _ in range(num_dice)]
    return rolls

def display_dice(rolls):
    """Display dice faces side by side with colors."""
    for row in range(5):
        parts = []
        for i, roll in enumerate(rolls):
            color = COLORS[i % len(COLORS)]
            parts.append(f"{color}{DICE_FACES[roll][row]}{RESET}")
        print("  ".join(parts))

if __name__ == "__main__":
    print("Dice Roller")
    print("-" * 40)

    num_dice = int(input("How many dice? (1-3): "))
    num_dice = max(1, min(3, num_dice))

    results = roll_dice(num_dice)

    print()
    display_dice(results)
    print(f"\nResults: {results}")
    print(f"Total: {sum(results)}")
