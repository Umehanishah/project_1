#streamlit
import streamlit as st

st.set_page_config(page_title= "growth mindset project", project_icon="★")
st.title("Growth Mindset Challenge: Web App with Streamlit")

st.header ("🌠 Welcome to your Growth Journey!")
st.write("Embrace your power")

#quote section
st.header("Today`s Growth Mindset Quote")
st.write("Success is not final, failure is not fatal: It is the courage to continue that counts. -Winstone ")

st.header("What`s your challenge Today?")
user_input = st.text_input ("Describe a challenge you`re facing:")

#condition
if user_input:
    st.success(f"you are facing: {user_input}. keep pushing forward your goal!")
else:
    st.warning("tell us about your challenge to get started!")

#reflexing
st.header("Reflection on your learning")
reflection = st.text_area("write your reflection here")

if reflection:
    st.success(f"Great Insight! your relfection : {reflection}")
else:
    st.info("Reflection on past experience help you to grow! share your difficulties")


#acheivements
st.heaer("Celebrate your wins!")
acheivment = st.text_input("share something you`ve recently accomplished:")

if acheivment:
    st.success(f"Amazing! you achieved {acheivment}")
else:
    st.info("Big or small, every acheivment counts! share one now")

#footer
st.write("- - -")
st.write("Keep believing in yourself.")
st.write("**Created by Hanishah**")
