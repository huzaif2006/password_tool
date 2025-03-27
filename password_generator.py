import streamlit as st
import string
import random


def password_generator(length, use_digits, use_special_characters):
    characters = string.ascii_letters

    if use_digits:
        characters += string.digits   # if user tick the use digits check box this condtion will true and add digits in password

    if use_special_characters:
        characters += string.punctuation    #if user tick the special character check box this condtion will true and add special charcters in password


    return "".join(random.choice(characters) for _ in range(length))


st.title("Password Generator")

length = st.slider("select password length", min_value=6, max_value=20, value=8)

use_digits = st.checkbox("Include digits")

use_special_characters = st.checkbox("Include special character")

if st.button("generate password"):
    password = password_generator(length, use_digits, use_special_characters)
    st.code(f"Your generated password is {password}")