import re

def password_strength(password):
    # Define strength criteria
    length_criteria = len(password) >= 8
    upper_case_criteria = re.search(r'[A-Z]', password) is not None
    lower_case_criteria = re.search(r'[a-z]', password) is not None
    digit_criteria = re.search(r'\d', password) is not None
    special_char_criteria = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None

    # Calculate strength score
    score = sum([length_criteria, upper_case_criteria, lower_case_criteria,
                 digit_criteria, special_char_criteria])

    # Determine strength level
    if score <= 2:
        strength = "Weak"
    elif score == 3:
        strength = "Medium"
    else:
        strength = "Strong"

    return strength, score

def suggest_stronger_password(password):
    # Simple suggestions for stronger passwords
    suggestions = []
    if len(password) < 8:
        suggestions.append("Add more characters (at least 8).")
    if not re.search(r'[A-Z]', password):
        suggestions.append("Include at least one uppercase letter.")
    if not re.search(r'[a-z]', password):
        suggestions.append("Include at least one lowercase letter.")
    if not re.search(r'\d', password):
        suggestions.append("Include at least one digit.")
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        suggestions.append("Include at least one special character.")

    return suggestions

if __name__ == "__main__":
    user_password = input("Enter a password to check its strength: ")
    
    strength, score = password_strength(user_password)
    print(f"Password Strength: {strength} (Score: {score}/5)")

    if strength == "Weak" or strength == "Medium":
        suggestions = suggest_stronger_password(user_password)
        print("Suggestions to strengthen your password:")
        for suggestion in suggestions:
            print(f"- {suggestion}")