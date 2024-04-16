from openai import OpenAI
import streamlit as st

# Read the API Key and Setup an OpenAI Client
f = open("keys/.openai_api_key.txt")
key = f.read()
client = OpenAI(api_key=key)

st.title("👨‍💻AI Code Reviewer")
st.subheader("Detect bugs 🪲 in code and write the corrected code ☑️")

# Take User's Input
prompt = st.text_area("Chat with AI Code Reviewer...", 
                      placeholder="Enter your message here")

# If the button is clicked, generate responses
if st.button("Generate") == True:
    response = client.chat.completions.create(
      model="gpt-3.5-turbo-0301",
      messages=[
        {"role": "system", "content": "As an Expert in code review.Identify any bugs or errors and provide the corrected code."},
        {"role": "user", "content": prompt}
      ]
    )

    # Print the response on Web App
    st.write(response.choices[0].message.content)