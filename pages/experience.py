# Author: Victor V. Vu
# File: experience.py
# Description: Experience page for Victor's portfolio website
# Copyright (C) 2024 Victor V. Vu
# License: GNU GPL v3 - See https://www.gnu.org/licenses/gpl-3.0.en.html

from nicegui import ui
from components import *

# Constants for repeated styles
LABEL_STYLE = 'color: #FFFFFF;'
TITLE_STYLE = 'color: #FFFFFF; font-size: 32px;'
BOLD_LABEL_STYLE = 'color: #FFFFFF; font-weight: bold;'
COLUMN_STYLE = 'align-items: center; text-align: center;'
LOTTIE_STYLE = 'height: 400px;'

def experience_page(): # Function to render the experience page
    vu_header() # header function
    inject_ui() # CSS effects

    with ui.row().style('justify-content: center; width: 100%'): # Center the title
        ui.label('Relevant Experience').style(TITLE_STYLE)
    inject_lottie() # inject lottie animation

    lottie_1 = 'https://assets6.lottiefiles.com/packages/lf20_ne6kcqfz.json' 
    with ui.row().style('justify-content: center; width: 100%;'): 
        with ui.column().classes('about-me').style(COLUMN_STYLE): # Column for the first experience
            ui.html(f'''<lottie-player src="{lottie_1}" loop autoplay style="{LOTTIE_STYLE}"></lottie-player>''') # play animation
            ui.label('Instructional Student Assistant | CSUF - Department of Engineering and Computer Science').style(BOLD_LABEL_STYLE)
            ui.label('(January 2023 - May 2023)').style(LABEL_STYLE)
            ui.label('- Supported 60+ students enrolled in Computer Architecture and Systems Programming.').style(LABEL_STYLE)
            ui.label('- Evaluated software developed in x86-64 Assembly, C++, and C.').style(LABEL_STYLE)
            ui.label('- Provided extensive feedback on code design.').style(LABEL_STYLE)
            ui.label('- Facilitated study sessions to reinforce course understanding.').style(LABEL_STYLE)

    lottie_2 = 'https://assets3.lottiefiles.com/packages/lf20_6ft9bypa.json'
    with ui.row().style('justify-content: center; width: 100%;'):
        with ui.column().classes('about-me').style(COLUMN_STYLE): # Column for the second experience
            ui.html(f'''<lottie-player src="{lottie_2}" loop autoplay style="{LOTTIE_STYLE}"></lottie-player>''') 
            ui.label('C# Peer Programming Tutor  | CSUF - Department of Engineering and Computer Science').style(BOLD_LABEL_STYLE)
            ui.label('(August 2022 - December 2022)').style(LABEL_STYLE)
            ui.label('- Tutored 30+ peers enrolled in C# GUI Programming.').style(LABEL_STYLE)
            ui.label('- Debugged various logical errors from student programs, improving grades by 10%.').style(LABEL_STYLE)
            ui.label('- Presented additional lecture materials on optimizing collision algorithms.').style(LABEL_STYLE)
            ui.label('- Coordinated online meetings, encouraging collaboration.').style(LABEL_STYLE)
    vu_footer() # call footer function

@ui.page('/experience') # Route to experience page
def experience():
    experience_page()