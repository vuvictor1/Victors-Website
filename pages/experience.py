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

# Constants for repeated styles
label_style = 'color: #FFFFFF;'
title_style = 'color: #FFFFFF; font-size: 32px;'
bold_label_style = 'color: #FFFFFF; font-weight: bold;'
column_style = 'align-items: center; text-align: center;'
lottie_style = 'height: 400px;'

def experience_page(): # Function to render the experience page
    vu_header() # header function
    inject_ui() # CSS effects

    with ui.row().style('justify-content: center; width: 100%'): # Center the title
        ui.label('Relevant Experience').style(title_style)
    inject_lottie() # inject lottie animation

    lottie_1 = 'https://assets6.lottiefiles.com/packages/lf20_ne6kcqfz.json' 
    with ui.row().style('justify-content: center; width: 100%;'): 
        with ui.column().classes('about-me').style(column_style): # Column for the first experience
            ui.html(f'''<lottie-player src="{lottie_1}" loop autoplay style="{lottie_style}"></lottie-player>''') # play animation
            ui.label('Instructional Student Assistant | CSUF - Department of Engineering and Computer Science').style(bold_label_style)
            ui.label('(January 2023 - May 2023)').style(label_style)
            ui.label('- Supported 60+ students enrolled in Computer Architecture and Systems Programming.').style(label_style)
            ui.label('- Evaluated software developed in x86-64 Assembly, C++, and C.').style(label_style)
            ui.label('- Provided extensive feedback on code design.').style(label_style)
            ui.label('- Facilitated study sessions to reinforce course understanding.').style(label_style)

    lottie_2 = 'https://assets3.lottiefiles.com/packages/lf20_6ft9bypa.json'
    with ui.row().style('justify-content: center; width: 100%;'):
        with ui.column().classes('about-me').style(column_style): # Column for the second experience
            ui.html(f'''<lottie-player src="{lottie_2}" loop autoplay style="{lottie_style}"></lottie-player>''') 
            ui.label('C# Peer Programming Tutor  | CSUF - Department of Engineering and Computer Science').style(bold_label_style)
            ui.label('(August 2022 - December 2022)').style(label_style)
            ui.label('- Tutored 30+ peers enrolled in C# GUI Programming.').style(label_style)
            ui.label('- Debugged various logical errors from student programs, improving grades by 10%.').style(label_style)
            ui.label('- Presented additional lecture materials on optimizing collision algorithms.').style(label_style)
            ui.label('- Coordinated online meetings, encouraging collaboration.').style(label_style)
    vu_footer() # call footer function

@ui.page('/experience') # Route to experience page
def experience():
    experience_page()