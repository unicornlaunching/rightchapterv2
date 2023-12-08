import streamlit as st
import openai
import toml
from bokeh.models.widgets import Button, Div
from bokeh.layouts import column
from bokeh.models import CustomJS
from streamlit_bokeh_events import streamlit_bokeh_events

# Load API key from the .toml file
config = toml.load("config.toml")
openai.api_key = config["openai"]["api_key"]

# Create the Speak button and timer display
stt_button = Button(label="Speak", width=100)
timer_display = Div(text="Timer: 120")
transcription_display = st.empty()  # A placeholder to display the transcription

# (Previous JavaScript code for the speech-to-text functionality remains the same)

# Layout for the button and timer display
layout = column(stt_button, timer_display)

# Event handling in Streamlit
result = streamlit_bokeh_events(
    layout,
    events="GET_TEXT",
    key="listen",
    refresh_on_update=False,
    override_height=200,
    debounce_time=0)

if result:
    if "GET_TEXT" in result:
        transcript = result.get("GET_TEXT")
        transcription_display.text(transcript)

        # Prompt template for turning the transcript into a book chapter
        prompt = f"Turn the following transcript into a chapter of a book:\nTitle: [Your Title Here]\nOpening Quote: [Your Quote Here]\n\n{transcript}"

        # Call OpenAI API to generate the book chapter
        response = openai.Completion.create(
          engine="text-davinci-003",  # or use "text-davinci-
