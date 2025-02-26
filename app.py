import streamlit as st

st.set_page_config(page_title="Growth Mindset Project", page_icon="★")
st.title("Growth Mindset Challenge: Web App with Streamlit")

st.header("🌠 Welcome to Your Growth Journey!")
st.write("Embrace your power.")

# Quote section
st.header("Today's Growth Mindset Quote")
st.write("Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill")

# Challenge input
st.header("What’s Your Challenge Today?")
user_input = st.text_input("Describe a challenge you’re facing:")

if user_input:
    st.success(f"You are facing: {user_input}. Keep pushing forward toward your goal!")
else:
    st.warning("Tell us about your challenge to get started!")

# Reflection section
st.header("Reflection on Your Learning")
reflection = st.text_area("Write your reflection here:")

if reflection:
    st.success(f"Great insight! Your reflection: {reflection}")
else:
    st.info("Reflecting on past experiences helps you grow! Share your thoughts.")

# Achievements section
st.header("Celebrate Your Wins!")
achievement = st.text_input("Share something you’ve recently accomplished:")

if achievement:
    st.success(f"Amazing! You achieved: {achievement}")
else:
    st.info("Big or small, every achievement counts! Share one now.")

# Footer
st.write("---")
st.write("Keep believing in yourself.")
st.write("**Created by Hanishah**")
