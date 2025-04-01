import streamlit as st
import string
import random
import re

# ---------------------- Password Generator Function ----------------------

def password_generator(length, use_digits, use_special_characters):
    characters = string.ascii_letters

    if use_digits:
        characters += string.digits  # Add digits if checkbox is selected

    if use_special_characters:
        characters += string.punctuation  # Add special characters if checkbox is selected

    return "".join(random.choice(characters) for _ in range(length))

# ---------------------- Password Strength Checker Function ----------------------

def password_strength(password_code):
    if len(password_code) < 8:
        return "Weak: Password is too short."
    
    has_digit = re.search(r"\d", password_code)
    has_letter = re.search(r"[A-Za-z]", password_code)
    has_special = re.search(f"[{re.escape(string.punctuation)}]", password_code)

    if has_letter and has_digit and has_special:
        return "Strong: Your password is very secure!"
    elif has_letter and has_digit:
        return "Moderate: Add special characters to make it stronger."
    else:
        return "Weak: Use a mix of letters, numbers, and special characters."

# ---------------------- Streamlit UI ----------------------

st.title("Password Generator")

option = st.radio("Select an option", ["Generate Password", "Check password strength"])

# Generate Password Section
if option == "Generate Password":
    length = st.slider("Select password length", min_value=6, max_value=20, value=8)
    use_digits = st.checkbox("Include digits")
    use_special_characters = st.checkbox("Include special characters")

    if st.button("Generate Password"):
        password = password_generator(length, use_digits, use_special_characters)
        st.code(f"Your generated password is: {password}")

# Check Password Strength Section
elif option == "Check password strength":
    password_code = st.text_input("Enter a password to check its strength:", type="password")

    if password_code:
        strength = password_strength(password_code)
        st.subheader(strength)
    else:
        st.error("Please enter the password.")
