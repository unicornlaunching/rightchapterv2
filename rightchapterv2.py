import streamlit as st
import openai
import toml

# Load API key from the .toml file
config = toml.load("config.toml")
openai.api_key = config["openai"]["api_key"]

st.title("Text to Book Chapter Converter")

# Text input for the user to input their text
user_input = st.text_area("Enter your text here:")

if st.button("Convert to Book Chapter"):
    if user_input:
        # Construct the prompt for the OpenAI API
        prompt = f"Create a book chapter with the following content:\n\n{text}\n\nInclude a title and an opening quote."

        response = openai.Completion.create(
            engine="text-davinci-003",  # or use "text-davinci-004" if available
            prompt=prompt,
            max_tokens=1024  # Adjust based on your requirements
        )

        # Display the result
        chapter = response.choices[0].text.strip()
        st.subheader("Generated Book Chapter")
        st.write(chapter)
    else:
        st.write("Please enter some text to convert.")
