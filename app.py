# #streamlit

# import streamlit as st

# st.set_page_config(page_title= "Growth Mindset Project ", Project_icon="🗝️")
# st.title("Gorwth Mindset Challenge: WEb App with Streamlit")

# st.header("♛Welcome to your Growth Journey!")
# st.write("Step into your potential! 🚀 This AI-powered journey helps you embrace challenges, grow from every mistake, and transform setbacks into comebacks. Reflect, rise, and celebrate your daily wins as you build an unstoppable growth mindset!")

# #Quotes part
# st.header("🌺Today's Growth Mindset Quote")
# st.write(" “Success isn't the end, and failure isn't the enemy — it's the courage to keep going that truly defines you”._Inspired by Winston Churchill_")

# st.header("☘what's Your challenge Today?")
# user_input = st.text_input("Describe a challenge you're facing:")

# #condition
# if user_input:
#     st.success(f"You're facing: {user_input}. Keep pushing forward towards your goal ✨ You've got this!")
# else:
#     st.warning("Tell us about your challenge to get started!")
   
# #reflectionpart
# st.header("Reflect on Your Learning")
# reflection = st.text_area("Write your reflection here:")
# if reflection:
#     st.success(f"⭐Great Insight! Your reflection: {reflection}")   
# else:
#     st.info("Reflecting on past experience help you grow! share your difficulties")

# #acheivement
# st.header("🎊Celebrate your wins!")
# acheivement = st.text_input("Share something you've recently accomplished:")

# if acheivement:
#     st.success(f"🏆Amazing! you achieve: {acheivement} ")
# else:
#     st.info("Big or small , every acheivement counts! share one now😇")
# #footer
# st.write(" _ _ _")
# st.write(" Keep going. Believe in yourself — growth takes time.✨")
# st.write("**©Created by Humema Israr**")

#streamlit

import streamlit as st

st.set_page_config(page_title="Growth Mindset Project", page_icon="🗝️")
st.title("🌱 Growth Mindset Challenge: Web App with Streamlit")

# Welcome section
st.header("♛ Welcome to Your Growth Journey!")
st.write(
    "Step into your potential! 🚀 This AI-powered journey helps you embrace challenges, "
    "learn from mistakes, and transform setbacks into comebacks. Reflect, rise, and celebrate "
    "your daily wins as you build an unstoppable growth mindset!"
)

# Quote Section
st.header("🌺 Today's Growth Mindset Quote")
st.markdown(
    "> *“Success isn't final, and failure isn't fatal — it's the courage to continue that counts.”*  \n"
    "_— Inspired by Winston Churchill_"
)

# Challenge Section
st.header("☘ What's Your Challenge Today?")
user_input = st.text_input("💭 Describe a challenge you're facing:")

if user_input:
    st.success(f"🌟 You're facing: **{user_input}**. Keep pushing forward toward your goal — you've got this! 💪")
else:
    st.warning("📌 Tell us about your challenge to get started!")

# Reflection Section
st.header("🪞 Reflect on Your Learning")
reflection = st.text_area("📝 What did you learn today? Share your thoughts:")

if reflection:
    st.success(f"⭐ Great insight! Your reflection: *{reflection}*")
else:
    st.info("🔍 Reflecting on past experiences helps you grow. Share your difficulties!")

# Achievement Section
st.header("🎊 Celebrate Your Wins!")
achievement = st.text_input("🏆 Share something you've recently accomplished:")

if achievement:
    st.success(f"👏 Amazing! You achieved: **{achievement}** 🎉")
else:
    st.info("✨ Big or small, every achievement counts! Share one now 😊")

# Footer
st.markdown("---")
st.markdown("💖 *Keep going. Believe in yourself — growth takes time.* ✨")
st.markdown("**© Created with love by Humema Israr**")