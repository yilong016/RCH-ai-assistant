import base64
import string
import streamlit as st
from pathlib import Path
import os
import json
from dotenv import load_dotenv
from utils.listing_voc_prompt import gen_listing_prompt, gen_voc_prompt
from utils.listing_voc_agents import create_listing

from PIL import Image

import logging
logger = logging.getLogger(__name__)

def main():
    language_options = ['English', 'Chinese']
    language_lable = st.sidebar.selectbox('Select Language', language_options)

    with st.container():
        asin = st.text_input("Amazon ASIN", 'B0BZYCJK89')

        result = st.button("Submit")

        if result:
            domain = "com"
            system_prompt, user_prompt  = gen_voc_prompt(asin, domain, language_lable)
            output = text_to_text(system_prompt, user_prompt)

            st.write(output)

if __name__ == '__main__':
    main()
