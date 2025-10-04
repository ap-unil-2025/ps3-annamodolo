"""
Bonus Challenge: Password Generator
Generate secure passwords with customizable options.
"""

import random
import string


def generate_password(length=12, use_uppercase=True, use_lowercase=True, use_digits=True, use_special=True):
    """
    Generate a random secure password based on the user's preferences.
    Ensures at least one character of each selected type is included.
    """
    if length < 4:
        raise ValueError("Password length must be at least 4 characters.")

    char_sets = []
    password_chars = []

    if use_uppercase:
        char_sets.append(string.ascii_uppercase)
        password_chars.append(random.choice(string.ascii_uppercase))
    if use_lowercase:
        char_sets.append(string.ascii_lowercase)
        password_chars.append(random.choice(string.ascii_lowercase))
    if use_digits:
        char_sets.append(string.digits)
        password_chars.append(random.choice(string.digits))
    if use_special:
        char_sets.append(string.punctuation)
        password_chars.append(random.choice(string.punctuation))

    if not char_sets:
        raise ValueError("At least one character type must be selected.")

    # Combine all chosen character sets
    all_chars = ''.join(char_sets)

    # Fill the rest of the password
    while len(password_chars) < length:
        password_chars.append(random.choice(all_chars))

    # Shuffle for randomness
    random.shuffle(password_chars)

    return ''.join(password_chars)



def password_strength(password):
    """
    Evaluate password strength based on length and character diversity.
    Returns a rating: Weak / Medium / Strong / Very Strong
    """
    length = len(password)
    score = 0

    if any(c.islower() for c in password):
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1
    if length >= 12:
        score += 1
    if length >= 16:
        score += 1

    if score <= 2:
        return "Weak"
    elif score == 3:
        return "Medium"
    elif score == 4 or score == 5:
        return "Strong"
    else:
        return "Very Strong"



def main():
    print("Password Generator")
    print("-" * 30)

    # Ask user for password length
    user_input = input("Password length (default 12): ").strip()
    length = int(user_input) if user_input.isdigit() else 12

    # Generate main password
    password = generate_password(length)
    print(f"\nGenerated Password: {password}")
    print(f"Strength: {password_strength(password)}")

    # Generate 3 alternative passwords
    print("\nAlternative passwords:")
    for i in range(1, 4):
        alt_password = generate_password(length)
        strength = password_strength(alt_password)
        print(f"{i}. {alt_password} ({strength})")


if __name__ == "__main__":
    main()