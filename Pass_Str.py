import streamlit as st
import re

# Apply Custom Styling for a Light Theme
st.markdown(
    """
    <style>
        body {
            background-color: #f9f9f9;
            color: black;
        }
        .stTextInput>div>div>input {
            background-color: #ffffff;
            color: black;
            border-radius: 5px;
            border: 1px solid #ddd;
            padding: 8px;
        }
        .stAlert {
            border-radius: 10px;
        }
        .title {
            text-align: center;
            color: #007BFF;
        }
        .subtitle {
            text-align: center;
            font-size: 18px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Page Title
st.markdown("<h1 class='title'>🔒 Password Strength Checker</h1>", unsafe_allow_html=True)
st.markdown("<h3 class='subtitle'>Check how strong your password is below</h3>", unsafe_allow_html=True)

# Password Input
password = st.text_input("🔑 Enter Password:", type="password")

# Initialize variables
feedback = []
score = 0

if password:
    # Check password length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be **at least 8 characters** long.")

    # Check uppercase and lowercase
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Password should contain **both uppercase and lowercase letters**.")

    # Check digits
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Password should contain **at least one number** (0-9).")

    # Check special characters
    if re.search(r"[_@!]", password):
        score += 1
    else:
        feedback.append("❌ Password should contain **at least one special character** (_ @ !).")

    # Display password strength
    if score == 4:
        st.success("✅ **Strong Password!** Your password is secure. 💪")
    elif score == 3:
        st.warning("🟡 **Medium Strength** Try adding more complexity for better security.")
    else:
        st.error("🔴 **Weak Password!** Improve your password using the suggestions below.")

    # Show feedback
    if feedback:
        st.markdown("### 🛠 Suggestions to Improve Password:")
        for tip in feedback:
            st.write(tip)
else:
    st.info("ℹ️ Please enter a password to check its strength.")

