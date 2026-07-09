import streamlit as st

st.title("The Identity Interface")

st.write("Enter your name and message, then click Transmit.")

user_name = st.text_input("Enter your Name")

user_message = st.text_input("Enter you Message")

if st.button("Transmit"):
    

    if user_name == "":
        st.error("Please provied your name.")
    elif user_message == "":
        st.error("Please type a message to transmit.")
    else:
        st.success(
            f"Transmission successfull! Greetings, {user_name}. We received your message: {user_message}"
        )

        token_count = len(user_message) / 4

        st.info(
            f"System Check : Your message will consume approximately {token_count} tokens from our context window."
        )