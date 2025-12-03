# Money Management Simulation Game

def main():
    print("Welcome to the Money Management Simulation!")
    print("You’ll be tested on your financial skills through 8 life situations.")
    print("Try to keep your money above 0 and grow your financial traits!\n")

    # Initialize variables
    money = 20
    responsible = 0
    kind = 0
    aware = 0
    mathematical = 0

    # Define list of situations with effects
    situations = [
        {
            "title": "🍋 Situation 1: The Lemonade Stand Kickoff",
            "goal": "Financial Responsibility",
            "setup": "You’ve just earned $20 from your first lemonade stand.",
            "choices": {
                "a": ("Spend $10 on fun stuff.", lambda m, s: (m - 10, s - 1)),
                "b": ("Save all your earnings.", lambda m, s: (m + 10, s + 1))
            },
            "trait": "responsible"
        },
        {
            "title": "🤏 Situation 2: The Brother’s Borrow",
            "goal": "Financial Kindness",
            "setup": "Your brother asks to borrow some money.",
            "choices": {
                "a": ("Lend half of your money.", lambda m, s: (m * 0.5, s + 1)),
                "b": ("Lend nothing.", lambda m, s: (m * 1.0, s - 1))
            },
            "trait": "kind"
        },
        {
            "title": "🫥 Situation 3: The Street Stranger",
            "goal": "Financial Awareness",
            "setup": "A stranger offers to double your money next week if you lend all of it today.",
            "choices": {
                "a": ("Give all your money.", lambda m, s: (0, s - 1)),
                "b": ("Keep your money.", lambda m, s: (m, s + 1))
            },
            "trait": "aware"
        },
        {
            "title": "🧐 Situation 4: The Payout Puzzle",
            "goal": "Mathematical Thinking",
            "setup": "You can take either a lump sum or daily payments.",
            "choices": {
                "a": ("Take $80 now.", lambda m, s: (m + 80, s - 1)),
                "b": ("Take $14 per day for 7 days.", lambda m, s: (m + 98, s + 1))
            },
            "trait": "mathematical"
        },
        {
            "title": "🥴 Situation 5: The Friendly IOU",
            "goal": "Financial Kindness",
            "setup": "A friend needs $20 and promises to repay $10.",
            "choices": {
                "a": ("Lend the $20.", lambda m, s: (m - 10, s + 1)),
                "b": ("Refuse to lend.", lambda m, s: (m, s - 1))
            },
            "trait": "kind"
        },
        {
            "title": "😮‍💨 Situation 6: The Deal Dilemma",
            "goal": "Mathematical Reasoning",
            "setup": "You spot two special offers.",
            "choices": {
                "a": ("Buy 10 for $18.", lambda m, s: (m - 18, s + 1)),
                "b": ("Buy 5 for $12.", lambda m, s: (m - 12, s - 1))
            },
            "trait": "mathematical"
        },
        {
            "title": "🎲 Situation 7: The Gamble or Guarantee",
            "goal": "Financial Responsibility",
            "setup": "You can take $50 now or risk for double next week.",
            "choices": {
                "a": ("Gamble and wait.", lambda m, s: (m - 100, s - 1)),
                "b": ("Take the safe $50.", lambda m, s: (m + 50, s + 1))
            },
            "trait": "responsible"
        },
        {
            "title": "🥸 Situation 8: The Mysterious Donation",
            "goal": "Financial Awareness",
            "setup": "A person asks you to donate 30% to an unverified college.",
            "choices": {
                "a": ("Decline to donate.", lambda m, s: (m, s + 1)),
                "b": ("Donate 30%.", lambda m, s: (m * 0.7, s - 1))
            },
            "trait": "aware"
        },
    ]

    # Begin the simulation
    for situation in situations:
        if money <= 0:
            print("\nYou’re out of money! Game over.\n")
            break

        print(f"\n{ situation['title'] }")
        print(f"Goal: { situation['goal'] }")
        print(f"Your current balance: ${money:.2f}")
        print(situation["setup"])
        print("Choices:")
        for key, (desc, _) in situation["choices"].items():
            print(f"  {key}) {desc}")

        choice = input("Select a or b: ").lower().strip()
        if choice not in ["a", "b"]:
            print("Invalid choice. Skipping this situation.")
            continue

        # Apply the result
        func = situation["choices"][choice][1]
        new_money, new_trait = func(money, 0)

        # Adjust variables dynamically
        if situation["trait"] == "responsible":
            responsible += new_trait
        elif situation["trait"] == "kind":
            kind += new_trait
        elif situation["trait"] == "aware":
            aware += new_trait
        elif situation["trait"] == "mathematical":
            mathematical += new_trait

        money = new_money

        # Check balance
        if money <= 0:
            print("\nYour money dropped to zero or below!")
            break

    # End of game summary
    print("\nEnd of game.")
    if money <= 0:
        print("You’re in debt! Game over.")
    else:
        print(f"Final balance: ${money:.2f}")

    print("\nFinal Trait Scores:")
    print(f"Responsible: {responsible}")
    print(f"Kind: {kind}")
    print(f"Aware: {aware}")
    print(f"Mathematical: {mathematical}")
    print("\nThanks for playing!")

if __name__ == "__main__":
    main()
