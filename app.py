from PIL import Image
import streamlit as st

LOGO = Image.open("./img/logo.png")

MARKDOWN_INTRO = """
Welcome to the **Melody Agents** project, a PoC that tries to connect crewAI and 
Suno AI. The project works like this:

1. You provide a **topic** and a music **genre**
2. One agent will conduct a **web research** about the topic, fetching all relevant
    information.
3. Another agent will take the web research, and will craft high quality lyrics. These 
    lyrics will be adapted to the specific **genre**.
4. The last agent, using a custom tool, will send the lyrics into Suno AI and return to 
    you after a while with the two proposed songs.
"""

st.set_page_config(page_title="Melody Agents", layout="centered", page_icon=LOGO)

st.markdown("<h1 style='text-align: center;'>Melody Agents</h1>", unsafe_allow_html=True)
st.image(LOGO)
st.markdown(MARKDOWN_INTRO)

st.markdown("---")

topic = st.text_input("Topic", "A song about Elon Musk's last tweet")
genre = st.text_input("Genre", "Rap")

