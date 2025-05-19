import streamlit as st
import openai
from openai import OpenAI

# Set up your OpenAI API client
api_key = "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"  # Don't expose your real API key in the code
client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=api_key,
)

# Streamlit UI
st.title("Ramakrihsna agent")
st.markdown("Ask any question, and get a response from the AI model!")

# Input field for user to enter a question
user_input = st.text_input("What is your question?")

# When the user presses 'Submit'
if st.button("Submit"):
    if user_input:
        with st.spinner("Getting response from AI..."):
            # Make the API call
            completion = client.chat.completions.create(
                extra_headers={
                    "HTTP-Referer": "<YOUR_SITE_URL>",  # Optional
                    "X-Title": "<YOUR_SITE_NAME>",      # Optional
                },
                extra_body={},
                model="qwen/qwen3-1.7b:free",
                messages=[{
                    "role": "user",
                    "content": user_input
                }]
            )
            response = completion.choices[0].message.content
            st.success("AI Response:")
            st.write(response)
    else:
        st.warning("Please enter a question.")
